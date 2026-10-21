import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/apply_edits.py'


class WhitelistEditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.apply = None
        if SCRIPT.exists():
            spec = importlib.util.spec_from_file_location('en_edits', SCRIPT)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            cls.apply = staticmethod(module.apply_plan)

    def setUp(self):
        self.assertTrue(SCRIPT.exists(), 'English whitelist patch helper is not implemented')

    def edit(self, text, old, new, rule='E2'):
        return {'start': text.index(old), 'end': text.index(old) + len(old),
                'old': old, 'new': new, 'rule': rule, 'trigger': 'Located rule match; meaning manually reviewed'}

    def test_empty_plan_preserves_every_character(self):
        text = '## 2. Methods\r\n\r\nSamples were analyzed at 37\u00a0°C [7].\r\n'
        self.assertEqual(self.apply(text, {'edits': []}), text)

    def test_only_declared_span_changes(self):
        text = 'We tested in order to compare models. The result may vary [7].'
        result = self.apply(text, {'edits': [self.edit(text, 'in order to', 'to')]})
        self.assertEqual(result, 'We tested to compare models. The result may vary [7].')

    def test_unknown_rule_is_rejected(self):
        text = 'A robust model.'
        with self.assertRaises(ValueError):
            self.apply(text, {'edits': [self.edit(text, 'robust', 'good', 'E99')]})

    def test_stale_source_and_overlap_are_rejected(self):
        text = 'in order to test'
        change = self.edit(text, 'in order to', 'to')
        bad = dict(change, old='different')
        for edits in ([bad], [change, change]):
            with self.subTest(edits=edits), self.assertRaises(ValueError):
                self.apply(text, {'edits': edits})

    def test_protected_markdown_math_citations_and_macros(self):
        for text, old in [
            ('## In order to test', 'In order to'),
            ('- in order to test', 'in order to'),
            ('| in order to | value |', 'in order to'),
            ('> in order to test', 'in order to'),
            ('Text `in order to` remains.', 'in order to'),
            ('```python\nx="in order to"\n```', 'in order to'),
            ('$in order to$ remains.', 'in order to'),
            ('See \\cite{in order to}.', 'in order to'),
            ('See [7] for details.', '[7]'),
            ('See (Smith et al., 2024) for details.', '(Smith et al., 2024)'),
            ('See https://example.org/in-order-to.', 'in-order-to'),
            ('"in order to" is quoted.', 'in order to')]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                self.apply(text, {'edits': [self.edit(text, old, 'to')]})

    def test_number_range_and_modality_changes_are_rejected(self):
        for text, old, new in [('Accuracy was 0.8.', '0.8', '0.9'),
                               ('The CI was 0.81–0.94.', '0.81–0.94', '0.81-0.94'),
                               ('It may improve.', 'may improve', 'improves'),
                               ('It was not significant.', 'not significant', 'significant')]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                self.apply(text, {'edits': [self.edit(text, old, new, 'E1')]})

    def test_author_date_citation_is_protected_even_when_year_is_unchanged(self):
        text = 'See (Smith et al., 2024) for details.'
        with self.assertRaises(ValueError):
            self.apply(text, {'edits': [self.edit(text, 'Smith', 'Jones', 'E1')]})

    def test_newlines_and_explicit_terms_are_protected(self):
        text = 'We use graph neural network.\r\nAnother paragraph.'
        for plan in [
            {'edits': [self.edit(text, '.\r\n', '. ')]},
            {'edits': [self.edit(text, 'graph neural network', 'GNN')], 'protected_terms': ['graph neural network']}]:
            with self.subTest(plan=plan), self.assertRaises(ValueError):
                self.apply(text, plan)

    def test_cli_preserves_source_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source, plan, output = root / 'source.md', root / 'plan.json', root / 'edited.md'
            text = 'We tested in order to compare.\r\n'
            source.write_bytes(text.encode('utf-8'))
            plan.write_text(json.dumps({'edits': [self.edit(text, 'in order to', 'to')]}), encoding='utf-8')
            command = [sys.executable, '-B', str(SCRIPT), str(source), '--plan', str(plan), '-o', str(output)]
            first = subprocess.run(command, capture_output=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(output.read_bytes(), b'We tested to compare.\r\n')
            self.assertEqual(source.read_bytes(), text.encode('utf-8'))
            second = subprocess.run(command, capture_output=True)
            self.assertNotEqual(second.returncode, 0)
            self.assertEqual(output.read_bytes(), b'We tested to compare.\r\n')


if __name__ == '__main__':
    unittest.main()
