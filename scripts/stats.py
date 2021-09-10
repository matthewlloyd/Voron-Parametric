#!/usr/bin/python3
#
# Example usage: python3 scripts/stats.py --root=/path/to/git/repos/

import datetime
import io
import os
import pathlib
import sys

import typer


REPOS = {
    'Voron-2': {
        'github': 'VoronDesign/Voron-2',
        'root': 'STLs',
        'branch': 'Voron2.4',
    },

    'Voron-Trident': {
        'github': 'VoronDesign/Voron-Trident',
        'root': 'STLs',
        'branch': 'main',
    },

    'Voron-0': {
        'github': 'VoronDesign/Voron-0',
        'root': 'STLs',
        'branch': 'Voron0.1',
    },
}

IGNORE_SUBSTRINGS = [
    'Legacy_Brackets',
    'Slice_Mosquito',
    'Slice Mosquito',
    'Mosquito_Toolhead',
]

MARKDOWN_MISSING = ':black_large_square:'
MARKDOWN_RECONSTRUCTED = ':white_check_mark:'

MARKDOWN_OUT = sys.stdout

def print_markdown(*args):
    global MARKDOWN_OUT
    print(*args, file=MARKDOWN_OUT)


def detect_type(path: str) -> str:
    for repo_type in REPOS:
        if f'/{repo_type}/' in path:
            return repo_type
    assert False, f'Unable to detect repo type for path {path}'
    return None


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


def analyze_repo(theirs: str, ours: str, repo_type: str, printout: bool):
    total_stls = 0
    total_stls_reconstructed = 0

    all_stls = set()
    missing = set()
    reconstructed = {}
    missing_by_size = []

    config = REPOS[repo_type]
    for stl_path in pathlib.Path(theirs).glob('**/*.stl'):
        theirs_full = str(stl_path)
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
            reconstructed[theirs_relative] = ours_full_f3d_canonicalized
        else:
            missing.add(theirs_relative)
            missing_by_size.append((theirs_relative, os.path.getsize(theirs_full)))

    total_stls = len(all_stls)
    total_stls_reconstructed = len(reconstructed)

    if printout:
        print('Reconstructed STLs:')
        print()
        for stl in sorted(reconstructed.keys()):
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
    total = len(reconstructed) + len(missing)
    percentage = len(reconstructed) * 100.0 / total
    print_markdown(f'## {repo_type}')
    title = f'{len(reconstructed)}/{total}'
    title = f'{title:>7s}'
    title = title.replace('/', '%2f').replace(' ', '%20')
    print_markdown(
        f'<img src="https://progress-bar.dev/{percentage:.0f}'
        f'?width=500&title_width=50&title={title}'
        f'"/>')
    print_markdown()
    print_markdown(
        f'<details markdown="1">'
        f'<summary markdown="1">Click to expand file tree...</summary>')
    print_markdown()

    all_stls = set(reconstructed.keys()).union(set(missing))
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
        _, file = os.path.split(path)
        is_complete = len(paths[path]['missing']) == 0
        line = '  ' * indent + '- ' + \
            (MARKDOWN_RECONSTRUCTED if is_complete else MARKDOWN_MISSING)
        line += ' '
        line += file[:-4] if file.endswith('.stl') else file
        total_reconstructed = len(paths[path]["reconstructed"])
        total = len(paths[path]["missing"].union(paths[path]["reconstructed"]))
        percentage = total_reconstructed * 100. / total
        line += f' ({total_reconstructed}/{total}, {percentage:.0f}%)'
        print_markdown(line)
        for leaf in sorted(paths[path]['reconstructed_leaf'].union(paths[path]['missing_leaf'])):
            indent = leaf.count('/')
            leaf_root, file = os.path.split(leaf)
            is_complete = leaf in paths[path]['reconstructed_leaf']
            line = '  ' * indent + '- ' + \
                (MARKDOWN_RECONSTRUCTED if is_complete else MARKDOWN_MISSING)
            line += ' '
            file_root = file[:-4] if file.endswith('.stl') else file
            if is_complete:
                file_f3d = reconstructed[leaf]
                if os.path.islink(file_f3d):
                    # follow symbolic links
                    file_f3d = os.path.normpath(
                        os.path.join(repo_type, leaf_root, os.readlink(file_f3d)))
                # [Filament Card Caddy 25](Voron-2/TEST_PRINTS/Filament_Card_Caddy_25.f3d)
                line += f'[{file_root}]({file_f3d.replace(" ", "%20")})'
            else:
                line += file_root
            # add link to STL
            links = []
            links.append(
                f'[stl](https://github.com/VoronDesign/{repo_type}'
                f'/blob/{REPOS[repo_type]["branch"]}'
                f'/{REPOS[repo_type]["root"]}'
                f'/{leaf_root.replace(" ", "%20")}/{file_root.replace(" ", "%20")}.stl)')
            if is_complete:
                links.append(f'[f3d]({file_f3d.replace(" ", "%20")})')
            line += ' (' + ', '.join(links) + ')'
            print_markdown(line)
    print_markdown('</details>')


def main(root: str = None,
         repo: str = None,
         markdown: bool = False,
         readme: bool = False):
    global MARKDOWN_OUT
    assert root is not None, f'Must specify --root'
    repo_types = [repo] if repo is not None else REPOS.keys()
    if readme:
        markdown_stringio = io.StringIO()
        MARKDOWN_OUT = markdown_stringio
    if markdown:
        print_markdown('<!-- BEGIN_STATS generated by scripts/stats.py, do not edit -->')
        print_markdown(
            f'# Progress '
            f'(as of {datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")})')
        print_markdown()
    for repo_type in repo_types:
        theirs = os.path.join(root, repo_type) + '/'
        ours = os.path.join('.', repo_type)
        assert os.path.exists(ours), f'Unable to locate path for "ours" for {repo_type}'
        reconstructed, missing = analyze_repo(theirs, ours, repo_type, printout=not markdown)
        if markdown:
            render_to_markdown(repo_type, reconstructed, missing)
            print_markdown()
    if markdown:
        print_markdown('<!-- END_STATS -->')
    if readme:
        markdown_text = markdown_stringio.getvalue()
        lines = open('README.md', 'r').read().split('\n')
        begin_line = None
        end_line = None
        for i, line in enumerate(lines):
            if 'BEGIN_STATS' in line:
                begin_line = i
            elif 'END_STATS' in line:
                end_line = i
        assert begin_line and end_line, 'Unable to find BEGIN_STATS and END_STATS in README.md'
        lines = lines[:begin_line] + markdown_text.split('\n')[:-1] + lines[end_line+1:]
        open('README.md', 'w').write('\n'.join(lines))


if __name__ == '__main__':
    typer.run(main)
