"""Offline regressions for portable Receipts skill packaging."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from build_prompt import render
from validate import check


class ReceiptsTests(unittest.TestCase):
    def test_validation(self):
        self.assertEqual(check(), [])

    def test_generated_prompt(self):
        self.assertEqual((ROOT / 'PROMPT.md').read_text(encoding='utf-8'), render())

    def test_canonical_protocol_present(self):
        protocol = (ROOT / 'skills/receipts/references/PROTOCOL.md').read_text(encoding='utf-8').strip()
        self.assertIn(protocol, render())
        self.assertIn('references/PROTOCOL.md', (ROOT / 'skills/receipts/SKILL.md').read_text(encoding='utf-8'))

    def test_reply_requires_explicit_request(self):
        self.assertIn('Do not automatically write a public response.', render())
        self.assertIn('Explicitly prohibited:', render())
        self.assertIn('No AI-specific rule located', render())

    def test_prompt_self_contained(self):
        self.assertIn('no repository access or installed skill is necessary', render())
        self.assertIn('## Embedded reference: Evidence standards', render())
        self.assertIn('## Embedded reference: Research branch strategy', render())
        self.assertIn('## Embedded reference: Optional public response and rule checks', render())


if __name__ == '__main__':
    unittest.main()