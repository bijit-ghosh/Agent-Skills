"""Dependency-free checks for this repository's intentionally simple skill format."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    errors = []
    catalog = json.loads((root / 'catalog.json').read_text(encoding='utf-8'))
    names = [entry['name'] for entry in catalog['skills']]
    discovered = {p.parent.name for p in root.glob('*/SKILL.md')}
    if len(names) != len(set(names)) or set(names) != discovered:
        errors.append('Catalog must enumerate every skill exactly once')
    for entry in catalog['skills']:
        name = entry['name']
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64 or entry['path'] != name:
            errors.append(f'Invalid catalog name/path: {name}')
            continue
        path = root / name / 'SKILL.md'
        if not path.is_file():
            errors.append(f'Missing {path}')
            continue
        text = path.read_text(encoding='utf-8')
        parts = text.split('---', 2)
        if len(parts) != 3 or parts[0].strip():
            errors.append(f'{name}: missing frontmatter')
            continue
        fields = {}
        for line in parts[1].strip().splitlines():
            key, sep, value = line.partition(':')
            if sep and not line.startswith(' '):
                value = value.strip()
                fields[key] = json.loads(value) if value.startswith('"') else value
        if fields.get('name') != name or not fields.get('description'):
            errors.append(f'{name}: name/description missing or inconsistent')
        if fields.get('description') != entry['description']:
            errors.append(f'{name}: catalog description differs')
        for doc in (root / name).rglob('*.md'):
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', doc.read_text(encoding='utf-8')):
                if '://' in target or target.startswith('#'):
                    continue
                resolved = (doc.parent / target.split('#')[0]).resolve()
                if not resolved.is_relative_to((root / name).resolve()) or not resolved.exists():
                    errors.append(f'{doc.relative_to(root)}: missing or non-standalone reference {target}')
    return errors


if __name__ == '__main__':
    problems = validate()
    print('\n'.join(problems) if problems else 'PASS: catalog, skill metadata, and standalone references')
    raise SystemExit(bool(problems))
