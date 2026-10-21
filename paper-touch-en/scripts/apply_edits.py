"""Apply reviewed E1-E6 span edits while preserving unmatched UTF-8 text."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

RULES = frozenset({'E1', 'E2', 'E3', 'E4', 'E5', 'E6'})
NUMBER = re.compile(r'(?<!\w)[+−-]?\d+(?:[.,]\d+)*(?:[–—-]\d+(?:[.,]\d+)*)?%?')
MODAL = re.compile(
    r'\b(?:\w+n[\x27’]t|cannot|may|might|could|can|must|shall|should|will|would|'
    r'not|no|never|neither|nor|none|unless|without|unlikely|likely|possibly|probably|'
    r'perhaps|potentially|yet|already)\b', re.I)
UNIT = (r'(?:[yzafpnµμumcdhkMGTPEZY]?(?:mol|kat|Hz|Pa|Wb|Bq|Gy|Sv|rad|sr|eV|Da|'
        r'Ohm|Ω|[msAgKJWNVCFHLST])|°[CF]|%)'
        r'(?:\^?[+−-]?\d+|[⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻]+)?')
MEASUREMENT = re.compile(
    NUMBER.pattern + r'[ \t\u00a0]*' + UNIT +
    r'(?:[ \t\u00a0]*[/·⋅*][ \t\u00a0]*' + UNIT + r')*(?!\w)')
PROTECTED = [
    r'(`+)[^\r\n]*?\1',
    r'\$\$[\s\S]*?\$\$|(?<!\\)\$[^\r\n$]*\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)',
    r'\\[a-zA-Z]+\*?(?:\[[^\]\r\n]*\])?(?:\{[^{}\r\n]*\})+',
    r'\\begin\{(equation\*?|align\*?|tabular|verbatim)\}[\s\S]*?\\end\{\1\}',
    r'https?://[^\s<>]+', r'!?\[[^\]\r\n]*\]\([^\r\n)]*\)',
    r'\[\d+(?:\s*[,;–-]\s*\d+)*\]',
    r'\((?=[^()\r\n]*\b(?:19|20)\d{2}[a-z]?\b)[^()\r\n]*\)',
    r'"[^"\r\n]*"|“[^”\r\n]*”|‘[^’\r\n]*’',
    r"(?<![\w\\])'(?!\s)(?:[^'\r\n]|(?<=\w)'(?=\w))*?(?<!\s)'(?!\w)",
]


def protected_spans(text, plan):
    spans, fence, block_start, offset = [], None, None, 0
    for line in text.splitlines(keepends=True):
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence):
                spans.append((block_start, offset + len(line)))
                fence, block_start = None, None
        elif marker:
            fence, block_start = marker[1], offset
        elif re.match(r'^\s*(?:#{1,6}\s|>|\||[-+*]\s|\d+[.)]\s)', line):
            spans.append((offset, offset + len(line)))
        offset += len(line)
    if fence:
        spans.append((block_start, len(text)))
    for pattern in PROTECTED:
        spans.extend(match.span() for match in re.finditer(pattern, text))
    spans.extend(match.span() for match in MEASUREMENT.finditer(text))
    for term in plan.get('protected_terms', []):
        if not isinstance(term, str) or not term:
            raise ValueError('Protected terms must be nonempty text')
        spans.extend(match.span() for match in re.finditer(re.escape(term), text))
    for start, end in plan.get('protected_ranges', []):
        if type(start) is not int or type(end) is not int or not 0 <= start < end <= len(text):
            raise ValueError('Invalid protected range')
        spans.append((start, end))
    return spans


def apply_plan(original, plan):
    edits = plan['edits']
    if not isinstance(original, str) or not isinstance(edits, list):
        raise ValueError('Expected original text and an edits list')
    protected = protected_spans(original, plan)
    validated = []
    for edit in edits:
        start, end = edit['start'], edit['end']
        old, new = edit['old'], edit['new']
        if edit['rule'] not in RULES or not isinstance(edit.get('trigger'), str) or not edit['trigger'].strip():
            raise ValueError('Every edit needs an allowed rule and a concrete trigger')
        if type(start) is not int or type(end) is not int or not 0 <= start < end <= len(original):
            raise ValueError('Invalid edit offsets')
        if not isinstance(old, str) or not isinstance(new, str) or old != original[start:end]:
            raise ValueError('Edit anchor differs from the original')
        if old == new:
            raise ValueError('Unnecessary no-op edit')
        if any(ch in old or ch in new for ch in '\r\n'):
            raise ValueError('Line and paragraph boundaries are protected')
        if any(start < right and end > left for left, right in protected):
            raise ValueError('Edit intersects protected material')
        if NUMBER.findall(old) != NUMBER.findall(new):
            raise ValueError('Numerical literal or range changed')
        if [x.lower() for x in MODAL.findall(old)] != [x.lower() for x in MODAL.findall(new)]:
            raise ValueError('Negation or modality changed')
        validated.append((start, end, new))
    validated.sort()
    output, cursor = [], 0
    for start, end, new in validated:
        if start < cursor:
            raise ValueError('Edits overlap')
        output.extend((original[cursor:start], new))
        cursor = end
    output.append(original[cursor:])
    result = ''.join(output)
    # Compare full context too: a partial-word patch can hide a protected token
    # from checks confined to the old/new replacement strings.
    if [x.lower() for x in MODAL.findall(original)] != [x.lower() for x in MODAL.findall(result)]:
        raise ValueError('Negation, modality or research-state marker changed')
    if MEASUREMENT.findall(original) != MEASUREMENT.findall(result):
        raise ValueError('Measured value or unit changed')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('--plan', type=Path, required=True)
    parser.add_argument('-o', '--output', type=Path, required=True)
    args = parser.parse_args()
    if args.source.suffix.lower() not in {'.txt', '.md', '.tex', '.ltx'}:
        parser.error('Source must be a supported UTF-8 text file, not a binary container')
    try:
        data = args.source.read_bytes()
        if data.startswith((b'PK\x03\x04', b'%PDF-')) or b'\x00' in data:
            raise ValueError('Binary input is not supported')
        original = data.decode('utf-8')
        plan = json.loads(args.plan.read_text(encoding='utf-8-sig'))
        result = apply_plan(original, plan)
        with args.output.open('xb') as stream:
            stream.write(result.encode('utf-8'))
        print(json.dumps({'edits_applied': len(plan['edits']), 'source_sha256': hashlib.sha256(data).hexdigest(),
                          'output': str(args.output), 'meaning_verified': False}, ensure_ascii=True))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print('Patch refused: ' + str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
