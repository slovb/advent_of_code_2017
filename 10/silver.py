def calc(size, lengths):
    data = range(size)
    pos = 0
    skip = 0
    for length in lengths:
        for i in range(length // 2):
            x = (pos + i) % size
            y = (pos + length - i - 1) % size
            data[x], data[y] = data[y], data[x]
        pos = (pos + length + skip) % size
        skip += 1
    return data[0] * data[1]

def read(filename):
    with open(filename, 'r') as f:
        line = map(int, f.readline().rstrip().split(','))
        return line

def main(filename):
    print calc(256, read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)

