import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/apply_edits.py'
spec = importlib.util.spec_from_file_location('protection_edits', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def plan(text, old, new, rule='E2'):
    start = text.index(old)
    return {'edits': [{'start': start, 'end': start + len(old), 'old': old,
                       'new': new, 'rule': rule, 'trigger': 'Controlled regression fixture'}]}


class ProtectionTests(unittest.TestCase):
    def test_units_cannot_change_even_when_digits_are_unchanged(self):
        for text, old, new in [
            ('The delay was 5 ms.', 'ms', 's'),
            ('The concentration was 2 mg/mL.', 'mg', 'g'),
            ('The samples were held at 37 °C.', '°C', '°F'),
            ('The speed was 4 m/s.', 'm/s', 'm'),
            ('The delay was 5 ms.', '5 ms', '5 s'),
        ]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                module.apply_plan(text, plan(text, old, new))

    def test_negation_and_modality_cannot_be_changed(self):
        for text, old, new in [
            ('The model cannot generalize.', 'cannot', 'can'),
            ("The model can't generalize.", "can't", 'can'),
            ('The model can’t generalize.', 'can’t', 'can'),
            ('The effect is unlikely.', 'unlikely', 'likely'),
            ('We will conduct an evaluation.', 'will', 'did'),
            ('We have not yet evaluated it.', 'not yet', 'already'),
        ]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                module.apply_plan(text, plan(text, old, new))

    def test_partial_token_edits_cannot_bypass_negation_guard(self):
        for text, old, new in [
            ('The model cannot generalize.', 'not', 'only'),
            ('It may improve.', 'ay', 'ust'),
        ]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                module.apply_plan(text, plan(text, old, new))

    def test_straight_single_quoted_text_is_protected(self):
        for text in [
            "The author wrote 'in order to compare models'.",
            "The author wrote 'the model's purpose is in order to compare'.",
            "The author wrote 'we can't test in order to compare'.",
        ]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                module.apply_plan(text, plan(text, 'in order to', 'to'))

    def test_apostrophes_do_not_hide_unquoted_prose(self):
        for text, expected in [
            ("The author's model was tested in order to compare results.",
             "The author's model was tested to compare results."),
            ("We can't omit controls in order to compare the authors' models.",
             "We can't omit controls to compare the authors' models."),
        ]:
            with self.subTest(text=text):
                self.assertEqual(module.apply_plan(text, plan(text, 'in order to', 'to')), expected)

    def test_all_six_existing_rule_examples_still_apply(self):
        cases = [
            ('It is worth noting that the samples were stored at 4 °C.',
             'It is worth noting that the', 'The', 'E1',
             'The samples were stored at 4 °C.'),
            ('The samples were randomized in order to reduce allocation bias.',
             'in order to', 'to', 'E2',
             'The samples were randomized to reduce allocation bias.'),
            ('We conducted an evaluation of the encoder on the test split.',
             'conducted an evaluation of', 'evaluated', 'E3',
             'We evaluated the encoder on the test split.'),
            ('Furthermore, additionally, we released the configuration files [3].',
             'additionally, ', '', 'E4',
             'Furthermore, we released the configuration files [3].'),
            ('The fitted value was approximately about 0.8 and may vary by site.',
             'about ', '', 'E5',
             'The fitted value was approximately 0.8 and may vary by site.'),
            ('The checker acts as a tireless assistant that flags missing citations.',
             'acts as a tireless assistant that flags', 'flags', 'E6',
             'The checker flags missing citations.'),
        ]
        for text, old, new, rule, expected in cases:
            with self.subTest(rule=rule):
                self.assertEqual(module.apply_plan(text, plan(text, old, new, rule)), expected)

    def test_legal_edits_preserve_nearby_units_and_research_state(self):
        text = 'We will test at 5 ms in order to compare; the model cannot yet generalize.'
        self.assertEqual(module.apply_plan(text, plan(text, 'in order to', 'to')),
                         'We will test at 5 ms to compare; the model cannot yet generalize.')

    def test_empty_plan_preserves_quotes_units_and_crlf(self):
        text = "\ufeffThe author's model cannot exceed 5 mg/mL.\r\n'in order to' stays.\r\n"
        self.assertEqual(module.apply_plan(text, {'edits': []}), text)

    def test_list_and_table_rows_remain_fully_protected(self):
        for text in ['- We tested in order to compare.\n', '| in order to | value |\n']:
            with self.subTest(text=text), self.assertRaises(ValueError):
                module.apply_plan(text, plan(text, 'in order to', 'to'))

    def test_cli_refuses_unsafe_patch_without_creating_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, patch, output = root / 'source.md', root / 'patch.json', root / 'output.md'
            text = 'The delay was 5 ms.\r\n'
            source.write_bytes(text.encode())
            patch.write_text(json.dumps(plan(text, 'ms', 's')), encoding='utf-8')
            result = subprocess.run([sys.executable, '-B', str(SCRIPT), str(source),
                                     '--plan', str(patch), '-o', str(output)], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(output.exists())
            self.assertEqual(source.read_bytes(), text.encode())


if __name__ == '__main__':
    unittest.main()
