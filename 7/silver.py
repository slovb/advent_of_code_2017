class Node:
    def __init__(self, key, weight, children = []):
        self.key = key
        self.weight = weight
        self.children = children
    def __str__(self):
        return "{} {}: {}".format(
            self.key,
            self.weight,
            ', '.join(self.children)
        )

def findRoot(nodes):
    node = nodes[0]
    parent = None
    while True:
        for potential in nodes:
            # find parent
            if node.key in potential.children:
                parent = potential
                break
        if parent == None:
            return node
        node = parent
        parent = None

def calc(nodes):
    return findRoot(nodes).key

def read(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        data = []
        for line in lines:
            d = line.split()
            key = d[0]
            weight = int(d[1].strip('(').strip(')'))
            children = []
            for c in d[3:]:
                children.append(c.strip(','))
            data.append(Node(key, weight, children))
        return data

def main(filename):
    print calc(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
