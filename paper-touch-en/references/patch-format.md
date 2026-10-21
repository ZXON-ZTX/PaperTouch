# Minimal file patches

Use the available Python 3.10+ launcher. Paths resolve from the skill directory in this example:

```text
python scripts/apply_edits.py draft.md --plan edits.json -o draft.cleaned.md
```

The source must be UTF-8 `.txt`, `.md`, `.tex` or `.ltx`, not Word/PDF. Output must be a new file. Character offsets count Unicode code points in the decoded original, including a BOM if present; they are not byte offsets. Read the actual original bytes without newline normalization before locating spans.

```json
{
  "edits": [
    {"start": 10, "end": 21, "old": "in order to", "new": "to", "rule": "E2", "trigger": "Exact purpose phrase; no author-style exception"}
  ],
  "protected_terms": ["graph neural network"],
  "protected_ranges": []
}
```

Offsets above illustrate the schema, not a ready-made patch for an unspecified source. Locate real offsets from the actual file. `old` must equal `original[start:end]`; edits must be nonempty, non-overlapping, and carry E1–E6 plus a concrete trigger reason. An empty edits list creates an identical copy.

The helper preserves all regions outside accepted spans exactly and refuses changes to recognized Markdown headings/lists/tables/block quotes/fences, inline code, URLs/links, common quoted strings, numeric citations, year-bearing parenthetical citations, common LaTeX macros and math spans. It also checks numerical literals/ranges, basic negation/modality tokens and line-break preservation. Add explicit `[start,end]` protected ranges and terminology for missed structures. The recognizer is deliberately conservative and is not a complete Markdown/LaTeX/quotation parser.

The plan still requires human/model judgment: a rule ID and a successful patch do not prove the trigger was appropriate, all protected spans were identified, or the meaning stayed equivalent. Review units, scope, causal relations, attribution, comparison, scientific claims and style exceptions manually. Reject any plan that needs a wider rewrite than the whitelist permits. No detector, API or network service is called.

## Protection details and regression tests

The helper continues to protect entire recognized Markdown list and table rows, headings and block quotes. It does not enable edits inside those rows. Preserve the existing E1–E6 scope: examples of tense/modality exceptions do not authorize additional transformations beyond the rule's stated trigger and meaning-preservation conditions.

Single-line straight single-quoted passages are also protected, including ordinary word-internal apostrophes such as `'the model's output'`. An apostrophe in unquoted `author's` or `can't` is not by itself an opening quotation. Nested, unbalanced, multiline or ambiguous quotations still need explicit protected ranges; automatic quote recognition is not a complete parser.

The helper protects recognized numeric measurements with common SI symbols/prefixes, °C/°F, %, and slash/dot/star compound units (for example `5 ms`, `2 mg/mL`, `4 m/s`). This is a limited symbol recognizer, not a complete unit system. Written-out units, domain-specific notation and other missed forms require explicit protected terms/ranges and manual review. Units without adjacent numeric values are not automatically covered by this recognizer.

Negation/modality checks include common contractions, `cannot`, and selected uncertainty/research-state markers, and compare the full source/result token sequences to catch partial-word edits. This is a lexical check, not a tense, scope or semantic-equivalence analysis. Preserving token sequences cannot prove preservation of scientific meaning.

Run the bundled tests from the skill directory with Python 3.10+:

```text
python -B -m unittest discover -s tests -v
```

The suite checks the original patch behavior, the six existing rule examples, refusal of unsafe unit/negation/quotation edits, apostrophes in ordinary prose, unchanged list/table protection, exact empty-plan preservation, and CLI refusal without creating an output. Rule examples are controlled fixtures, not evidence of effectiveness on real manuscripts or AI detectors.
