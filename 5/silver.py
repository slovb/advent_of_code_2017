def calc(steps):
    l = len(steps)
    i = 0; # index
    c = 0; # counter
    while i < l:
        steps[i] += 1
        i += steps[i] - 1
        c += 1
    return c

def read(filename):
    with open(filename, 'r') as f:
        return map(int, f.readlines())

def main(filename):
    print calc(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
