#!/usr/bin/python3
#
# Example usage: python3 scripts/stats.py --theirs=/path/to/git/repo/Voron-2/

import os
import pathlib
import typer


REPOS = {
    'Voron-2': {
        'github': 'VoronDesign/Voron-2',
        'root': 'STLs',
    }
}

IGNORE_SUBSTRINGS = [
    'Legacy_Brackets',
]


def detect_type(path: str) -> str:
    for repo_type in REPOS:
        if f'/{repo_type}/' in path:
            return repo_type
    assert False, f'Unable to detect repo type for path {path}'


def canonicalize(path: str) -> str:
    # B -> A
    path = path.replace('_b_', '_a_')
    return path


def analyze_repo(theirs: str, ours: str, repo_type: str):
    total_stls = 0
    total_stls_reconstructed = 0

    all_stls = set()
    missing = set()
    reconstructed = set()
    missing_by_size = []

    config = REPOS[repo_type]
    for p in pathlib.Path(theirs).glob('**/*.stl'):
        theirs_full = str(p)
        assert theirs_full.startswith(theirs)
        theirs_relative = theirs_full[len(theirs):]
        if theirs_relative.startswith(config['root'] + '/'):
            theirs_relative = theirs_relative[len(config['root'] + '/'):]
        ignored = False
        for pattern in IGNORE_SUBSTRINGS:
            if pattern in theirs_relative:
                ignored = True
                break
        if ignored:
            continue
        ours_full = os.path.join(ours, theirs_relative)
        assert ours_full.endswith('.stl')
        ours_full_f3d = ours_full[:-len('.stl')] + '.f3d'
        ours_full_f3d_canonicalized = canonicalize(ours_full_f3d)
        all_stls.add(theirs_relative)
        if os.path.exists(ours_full_f3d_canonicalized):
            reconstructed.add(theirs_relative)
        else:
            missing.add(theirs_relative)
            missing_by_size.append( (theirs_relative, os.path.getsize(theirs_full) ) )

    total_stls = len(all_stls)
    total_stls_reconstructed = len(reconstructed)
    total_missing = len(missing)

    print('Reconstructed STLs:')
    print()
    for stl in sorted(reconstructed):
        print(stl)

    print()
    print()
    print('Missing STLs:')
    print()
    for stl in sorted(missing):
        print(stl)

    print()
    print()
    print('Low-hanging fruit:')
    print()
    for stl, size in sorted(missing_by_size, key=lambda ss: ss[1])[:20]:
        print(f'{stl} [{size} bytes]')

    print()
    print()
    percentage = total_stls_reconstructed * 100.0 / total_stls
    print(f'{total_stls_reconstructed}/{total_stls} ({percentage:.1f}%) reconstructed')


def main(theirs: str = None, ours: str = None, repo_type: str = None):
    assert theirs is not None, f'Must specify --theirs'
    if repo_type is None:
        repo_type = detect_type(theirs)
    if ours is None:
        ours = f'./{repo_type}'
        assert os.path.exists(ours), f'Unable to guess path for "ours"'
    analyze_repo(theirs, ours, repo_type)


if __name__ == '__main__':
    typer.run(main)
