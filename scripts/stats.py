#!/usr/bin/python3
#
# Example usage: python3 scripts/stats.py --theirs=/path/to/git/repo/Voron-2/

import os
import pathlib
import re
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

MARKDOWN_MISSING = ':black_large_square:'
MARKDOWN_RECONSTRUCTED = ':white_check_mark:'


def detect_type(path: str) -> str:
    for repo_type in REPOS:
        if f'/{repo_type}/' in path:
            return repo_type
    assert False, f'Unable to detect repo type for path {path}'


def canonicalize(path: str) -> str:
    # B -> A
    path = path.replace('_b_', '_a_')
    # panel clips, clip_6mm -> clip_3mm
    path = path.replace('midspan_panel_clip_6mm_x3', 'midspan_panel_clip_3mm_x12')
    path = path.replace('corner_panel_clip_6mm_x4', 'corner_panel_clip_3mm_x12')
    # front idler tensioners are mirror images
    path = path.replace('tensioner_right', 'tensioner_left')
    # Z tensioners 9mm->6mm
    path = path.replace('z_tensioner_x4_9mm', 'z_tensioner_x4_6mm')
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

    return reconstructed, missing


def render_to_markdown(repo_type, reconstructed, missing):
    print('--------')
    print('Markdown')
    print('--------')
    print()

    total = len(reconstructed) + len(missing)
    percentage = len(reconstructed) * 100.0 / total
    print(f'### {repo_type} ({len(reconstructed)}/{total}, {percentage:.0f}%)')

    print()
    all_stls = set(reconstructed).union(set(missing))
    paths = {}
    for stl in sorted(all_stls):
        path, file = os.path.split(stl)
        path_parts = path.split('/')
        for i in range(len(path_parts), 0, -1):
            subpath = '/'.join(path_parts[:i])
            if subpath not in paths:
                paths[subpath] = {
                    'reconstructed': set(),
                    'missing': set(),
                    'reconstructed_leaf': set(),
                    'missing_leaf': set()
                }
            if stl in reconstructed:
                if i == len(path_parts):
                    paths[subpath]['reconstructed_leaf'].add(stl)
                paths[subpath]['reconstructed'].add(stl)
            else:
                if i == len(path_parts):
                    paths[subpath]['missing_leaf'].add(stl)
                paths[subpath]['missing'].add(stl)
    for path in sorted(paths.keys()):
        indent = path.count('/')
        p, file = os.path.split(path)
        is_complete = len(paths[path]['missing']) == 0
        line = '  ' * indent + '- ' + \
            (MARKDOWN_RECONSTRUCTED if is_complete else MARKDOWN_MISSING) \
            + ' ' + (file[:-4] if file.endswith('.stl') else file)
        total_reconstructed = len(paths[path]["reconstructed"])
        total = len(paths[path]["missing"].union(paths[path]["reconstructed"]))
        percentage = total_reconstructed * 100. / total
        line += f' ({total_reconstructed}/{total}, {percentage:.0f}%)'
        print(line)
        for leaf in sorted(paths[path]['reconstructed_leaf'].union(paths[path]['missing_leaf'])):
            indent = leaf.count('/')
            p, file = os.path.split(leaf)
            is_complete = leaf in paths[path]['reconstructed_leaf']
            line = '  ' * indent + '- ' + \
                (MARKDOWN_RECONSTRUCTED if is_complete else MARKDOWN_MISSING) + \
                ' ' + (file[:-4] if file.endswith('.stl') else file)
            print(line)


def main(theirs: str = None, ours: str = None, repo_type: str = None, markdown: bool = False):
    assert theirs is not None, f'Must specify --theirs'
    if repo_type is None:
        repo_type = detect_type(theirs)
    if ours is None:
        ours = f'./{repo_type}'
        assert os.path.exists(ours), f'Unable to guess path for "ours"'
    reconstructed, missing = analyze_repo(theirs, ours, repo_type)
    if markdown:
        render_to_markdown(repo_type, reconstructed, missing)


if __name__ == '__main__':
    typer.run(main)
