#!/usr/bin/python3

from collections import defaultdict
import hashlib
import os
import pathlib

import typer


from stats import REPOS

def main(root: str = None):
    assert root is not None, f'Must specify --root'
    files_by_hash = defaultdict(set)
    for repo_type in REPOS:
        theirs = os.path.join(root, repo_type) + '/'
        for stl_path in pathlib.Path(theirs).glob('**/*.stl'):
            md5_hash = hashlib.md5()
            md5_hash.update(open(stl_path, 'rb').read())
            files_by_hash[md5_hash.hexdigest()].add(str(stl_path))

    for _, files in files_by_hash.items():
        if len(files) == 1:
            continue
        print('\n'.join(sorted(files)))
        print()


if __name__ == '__main__':
    typer.run(main)
