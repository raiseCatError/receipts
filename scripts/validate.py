#!/usr/bin/env python3
"""Dependency-free format, safety-gate and synchronization validator."""
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_prompt import ROOT, render

SKILL = ROOT / 'skills' / 'receipts' / 'SKILL.md'
FILES = [
    'README.md', 'PROMPT.md', 'LICENSE', 'skills/receipts/SKILL.md',
    'skills/receipts/references/PROTOCOL.md',
    'skills/receipts/references/EVIDENCE.md',
    'skills/receipts/references/DISCOVERY.md',
    'skills/receipts/references/PUBLIC-REPLIES.md',
    'skills/receipts/assets/REPORT_TEMPLATE.md',
    'skills/receipts/assets/EVIDENCE_LEDGER_TEMPLATE.md',
    'skills/receipts/assets/CALLOUT_NOTES_TEMPLATE.md',
    'scripts/build_prompt.py', 'scripts/validate.py', 'scripts/package.py', 'tests/test_structure.py',
]


def check():
    errors = []
    for relative in FILES:
        if not (ROOT / relative).is_file():
            errors.append(f'Missing file: {relative}')
    if not SKILL.is_file():
        return errors
    skill = SKILL.read_text(encoding='utf-8')
    fm = re.match(r'\A---\n(?P<body>.*?)\n---\n', skill, re.S)
    if not fm:
        errors.append('Missing YAML frontmatter in SKILL.md')
        return errors
    fields = dict(re.findall(r'^([a-z][a-z-]*):\s*(.*)$', fm.group('body'), re.M))
    if fields.get('name') != 'receipts':
        errors.append('Skill name is not receipts')
    if not (1 <= len(fields.get('description', '')) <= 1024):
        errors.append('Description length is invalid')
    if len(skill.splitlines()) > 500:
        errors.append('SKILL.md longer than recommended 500 lines')
    for relative in re.findall(r'`((?:references|assets)/[^`]+\.md)`', skill):
        if not (SKILL.parent / relative).is_file():
            errors.append(f'Broken SKILL.md reference: {relative}')
    if (ROOT / 'PROMPT.md').is_file():
        prompt = (ROOT / 'PROMPT.md').read_text(encoding='utf-8')
        if prompt != render():
            errors.append('PROMPT.md out of sync')
        for label, phrase in [
            ('report-first', 'Do not automatically write a public response'),
            ('AI content restriction', 'Explicitly prohibited'),
            ('freshness', 'latest'),
            ('source counting', 'unique'),
            ('source injection', 'untrusted'),
            ('personal fit', 'user fit'),
            ('platform rules', 'community rules'),
        ]:
            if phrase.lower() not in prompt.lower():
                errors.append(f'Prompt missing gate: {label}')
    return errors


def main():
    errors = check()
    if errors:
        print('\n'.join('FAIL: ' + err for err in errors), file=sys.stderr)
        return 1
    print(f'OK: {len(FILES)} required files, valid frontmatter, local references, safety gates and prompt sync')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
