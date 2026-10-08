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
        return {
            line.strip().lower() for line in f
        } | {
            '275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f'
        } # ecair test file

def scan_file(fp: Path, known_hashes: set[str]):
    if not fp.is_file():
        return None, None

    hashed = hash_file(fp)

    return (hashed in known_hashes), hashed