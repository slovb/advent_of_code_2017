def calc(bank):
    mem = {}
    c = 0
    while tuple(bank) not in mem:
        mem.update({tuple(bank): c})
        c += 1
        # index of first maximal number
        i = 0
        for j,y in enumerate(bank):
            if (y > bank[i]):
                i = j
        # redistribute
        x = bank[i]
        bank[i] = 0
        while x > 0:
            i = (i + 1) % len(bank)
            bank[i] += 1
            x -= 1
    return c - mem[tuple(bank)]

def read(filename):
    with open(filename, 'r') as f:
        return map(int, f.readline().split())

def main(filename):
    print calc(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
