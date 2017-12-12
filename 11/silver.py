def reduction(ring, k1, k2, kres = None):
    l = len(ring)
    k1 %= l
    k2 %= l
    amount = min(ring[k1], ring[k2])
    ring[k1] -= amount
    ring[k2] -= amount
    if kres != None:
        kres %= l
        ring[kres] += amount
    return ring

def calc(steps):
    keys = ['nw', 'n', 'ne', 'se', 's', 'sw']
    totalSteps = {}
    for k in keys:
        totalSteps[k] = 0
    for s in steps:
        totalSteps[s] += 1
    ring = [totalSteps[k] for k in keys]
    before = ring
    l = -1
    while sum(ring) != l:
        l = sum(ring)
        for i in range(6):
            ring = reduction(ring, i, i+3)
            ring = reduction(ring, i, i+2, i+1)
    return sum(ring)

def read(filename):
    with open(filename, 'r') as f:
        line = f.readline().rstrip().split(',')
        return line

def main(filename):
    print calc(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
