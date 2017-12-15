def calc(key):
    hashes = []
    for i in range(128):
        hashes.append(knot(key, i))
    binaries = ['{0:128b}'.format(int(h, 16)) for h in hashes]
    
    total = 0
    from sets import Set
    seen = Set()
    for y, b in enumerate(binaries):
        for x in range(128):
            if b[x] == '1':
                coord = (x, y)
                if coord not in seen:
                    total += 1
                    fill(coord, seen, binaries)
    return total

def fill(coord, seen, binaries):
    if coord in seen:
        return
    x,y = coord
    if binaries[y][x] != '1':
        return
    seen.add(coord)
    if x > 0:
        fill((x-1, y), seen, binaries)
    if x < 127:
        fill((x+1, y), seen, binaries)
    if y > 0:
        fill((x, y-1), seen, binaries)
    if y < 127:
        fill((x, y+1), seen, binaries)


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
