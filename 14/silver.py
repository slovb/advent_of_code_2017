def calc(key):
    hashes = []
    for i in range(128):
        hashes.append(knot(key, i))
    binaries = ['{0:128b}'.format(int(h, 16)) for h in hashes]
    total = 0
    for b in binaries:
        row = b.replace('0', '.').replace('1', '#')
        total += row.count('#')
        #print row
    return total

def knot(key, row):
    combined = '{}-{}'.format(key, row)
    lengths = [ord(c) for c in combined]
    size = 256
    data = range(size)
    pos = 0
    skip = 0
    lengths += [17, 31, 73, 47, 23]
    repeats = 64
    for repeat in range(repeats):
        for length in lengths:
            for i in range(length // 2):
                x = (pos + i) % size
                y = (pos + length - i - 1) % size
                data[x], data[y] = data[y], data[x]
            pos = (pos + length + skip) % size
            skip += 1
    dense = []
    for i in range(16):
        j = i*16
        sub = data[j:j+16]
        dense.append(reduce((lambda x, y: x ^ y), sub))
    hexed = [format(x, '02x') for x in dense]
    return ''.join(hexed)

def main(key):
    print calc(key)

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
