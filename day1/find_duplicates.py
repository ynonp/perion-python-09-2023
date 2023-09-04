import hashlib
from collections import defaultdict
from pathlib import Path
from typing import Iterable

start = Path('/Users/ynonp/tmp/duplicates')


def only_files(pathlist: Iterable[Path]) -> Iterable[Path]:
    return filter(lambda p: p.is_file(), pathlist)


## Read files and build the list of hashes
files = defaultdict(list)
for file_path in only_files(start.rglob('*')):
    content = file_path.read_bytes()
    hash = hashlib.sha256(content).hexdigest()
    files[hash].append(file_path)


## Print out the results
for hash, file_paths in files.items():
    if len(file_paths) == 1:
        continue

    print(f'Hash: {hash}, File names: {file_paths}')

