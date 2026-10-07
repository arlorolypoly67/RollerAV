output = 'hashes.txt'

for filename in ['malicious_SHA256_hashes_aa.txt', 'malicious_SHA256_hashes_ab.txt', 'malicious_SHA256_hashes_ac.txt']:
    with open(filename, 'r') as f:
        data = f.readlines()

    with open(output, 'a') as f2:
        for line in data:
            if not line.startswith('#'):
                f2.write(line)

print('done')