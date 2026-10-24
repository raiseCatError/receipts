#!/usr/bin/env python3
"""Package the full repo and the standalone Agent Skills folder as ZIP archives."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import argparse

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / 'skills' / 'receipts'
IGNORE = {'__pycache__', '.DS_Store', '.git', 'dist', '.receipts'}


def package(tree, zip_path, prefix):
    paths = sorted(p for p in tree.rglob('*') if p.is_file() and not any(
        bit in IGNORE or bit.endswith('.pyc') for bit in p.relative_to(tree).parts
    ))
    with ZipFile(zip_path, 'w', compression=ZIP_DEFLATED, compresslevel=9) as z:
        for path in paths:
            z.write(path, arcname=(prefix / path.relative_to(tree)).as_posix())
    print(f'Created {zip_path} ({len(paths)} files, {zip_path.stat().st_size:,} bytes)')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output-dir', type=Path, default=ROOT / 'dist')
    args = p.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    package(ROOT, args.output_dir / 'receipts-repository.zip', Path('receipts'))
    package(SKILL, args.output_dir / 'receipts-agent-skill.zip', Path('receipts'))


if __name__ == '__main__':
    main()
