"""Install selected standalone skills from a local checkout. No network or overwrite."""
import argparse
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def install(names, destination, root=ROOT):
    catalog = json.loads((root / 'catalog.json').read_text(encoding='utf-8'))
    allowed = {entry['name'] for entry in catalog['skills']}
    if not names or len(names) != len(set(names)) or any(
            n not in allowed or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', n) for n in names):
        raise ValueError('Choose unique names from catalog.json')
    destination = Path(destination).expanduser().resolve()
    sources = [(root / n).resolve() for n in names]
    if any(destination == s or destination.is_relative_to(s) for s in sources):
        raise ValueError('Destination cannot be inside a source skill')
    targets = [destination / n for n in names]
    if any(p.exists() or p.is_symlink() for p in targets):
        raise FileExistsError('A destination skill already exists; no files changed')
    for source in sources:
        if not (source / 'SKILL.md').is_file() or any(p.is_symlink() for p in source.rglob('*')):
            raise ValueError('Source must be a complete skill without symbolic links')
    destination.mkdir(parents=True, exist_ok=True)
    created = []
    try:
        for source, target in zip(sources, targets):
            # Exclusive creation also protects against a concurrently installed target.
            target.mkdir()
            created.append(target)
            shutil.copytree(source, target, dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    except Exception:
        for target in reversed(created):
            shutil.rmtree(target)
        raise
    return targets


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', required=True, help='Explicit skill directory for your agent')
    parser.add_argument('skills', nargs='+')
    args = parser.parse_args()
    try:
        for installed in install(args.skills, args.dest):
            print(installed)
    except (ValueError, OSError) as error:
        parser.exit(1, f'Install refused: {error}\n')
