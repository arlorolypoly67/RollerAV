from pathlib import Path
from urllib.request import urlopen


BASE_URL = (
    'https://raw.githubusercontent.com/'
    'amitambekar510/Malicious-Hash-Threat-List/'
    'refs/heads/main/hashes/sha256/'
)

PARTITIONS = [
    'aa',
    'ab',
    'ac',
]

OUTPUT = Path('hashes.txt')
OUTPUT_TEMP = OUTPUT.with_suffix('.tmp')

def download_hashes() -> None:
    hashes = set()

    for partition in PARTITIONS:
        url = BASE_URL + 'malicious_SHA256_hashes_%s.txt' % partition

        print('Downloading %s...' % partition)

        with urlopen(url) as response:
            for line in response:
                line = line.decode('utf-8').strip()

                if line and not line.startswith('#'):
                    hashes.add(line.lower())

    with OUTPUT_TEMP.open('w') as f:
        for hashed in sorted(hashes):
            f.write(hashed + '\n')

    OUTPUT_TEMP.replace(OUTPUT)

    print('Downloaded %d hashes.' % len(hashes))


if __name__ == '__main__':
    download_hashes()