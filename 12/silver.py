def calc(key, adjacency):
    inspect = [key]
    from sets import Set
    seen = Set()
    while len(inspect) > 0:
        i = inspect.pop()
        seen.add(i)
        for j in adjacency[i]:
            if not j in seen:
                inspect.append(j)
    return len(seen)

def read(filename):
    with open(filename, 'r') as f:
        adjacency = {}
        lines = f.readlines()
        for line in lines:
            data = line.split(' ')
            key = int(data[0])
            adjacent = [int(a.rstrip(',')) for a in data[2:]]
            adjacency.update({key: adjacent})
        return adjacency

def main(filename):
    print calc(0, read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
