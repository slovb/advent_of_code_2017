def solve(components):
    indexBridges = build(components, 0, [])
    bridges = convert(components, indexBridges)
    values = [(len(b), sum([sum(c) for c in b])) for b in bridges]
    length = 0
    value = 0
    for l, v in values:
        if l > length:
            length = l
            value = v
        elif l == length and v > value:
            value = v
    return value
    """
    for b in bridges:
        print '{}: {}'.format(sum([sum(c) for c in b]), str(b))
    """

def build(components, current, chosen):
    indexBridges = [chosen]
    for k, c in enumerate(components):
        if k not in chosen:
            if c[0] == current:
                subBridges = build(components, c[1], chosen + [k])
                for b in subBridges:
                    indexBridges.append(b)
            if c[1] == current:
                subBridges = build(components, c[0], chosen + [k])
                for b in subBridges:
                    indexBridges.append(b)
    return indexBridges

def convert(components, indexBridges):
    bridges = []
    for ib in indexBridges:
        bridge = []
        for k in ib:
            bridge.append(components[k])
        bridges.append(bridge)
    return bridges

def read(filename):
    with open(filename, 'r') as f:
        return [tuple(map(int, r.split('/'))) for r in f.readlines()]

def main(filename):
    print solve(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)

