import hashlib
from pathlib import Path


def hash_file(fp: Path):
    hasher = hashlib.sha256()

    with fp.open('rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)

    return hasher.hexdigest()

def load_hashes(fp: Path):
    with fp.open('r') as f:
        return {line.strip().lower() for line in f}