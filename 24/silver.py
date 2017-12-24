def solve(components):
    """
    indexBridges = build(components, 0, [])
    bridges = convert(components, indexBridges)
    values = [sum([sum(c) for c in b]) for b in bridges]
    return max(values)
    """
    """
    for b in bridges:
        print '{}: {}'.format(sum([sum(c) for c in b]), str(b))
    """
    return recursive(components, (0, 0), [])

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
"""

def recursive(components, current, chosen):
    base = sum(current)
    strength = [base]
    for k, c in enumerate(components):
        if k not in chosen:
            if c[0] == current[1]:
                v = base + recursive(components, c, chosen + [k])
                strength.append(v)
            if c[1] == current[1]:
                v = base + recursive(components, c[::-1], chosen + [k])
                strength.append(v)
    return max(strength)

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

