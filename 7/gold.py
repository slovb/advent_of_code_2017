class Node:
    def __init__(self, key, weight, children = []):
        self.key = key
        self.weight = weight
        self.children = children
    def __str__(self):
        return "{} {}/{}".format(
            self.key,
            self.weight,
            self.total()
        )
    def total(self):
        w = self.weight
        for c in self.children:
            w += c.total()
        return w
    def isBalanced(self):
        if len(self.children) > 1:
            w = self.children[0].total()
            for c in self.children[1:]:
                if c.total() != w:
                    return False
        return True

def findRoot(nodes):
    node = nodes[0]
    parent = None
    while True:
        for potential in nodes:
            # find parent
            if node in potential.children:
                parent = potential
                break
        if parent == None:
            return node
        node = parent
        parent = None

def findUnbalance(node):
    # abuse that we know only one branch is unbalanced
    for c in node.children:
        if not c.isBalanced():
            return findUnbalance(c)
    return node

def calc(nodes):
    root = findRoot(nodes)
    node = findUnbalance(root)
    totals = {}
    for c in node.children:
        t = c.total()
        if t in totals:
            totals[t] += [c]
        else:
            totals.update({t: [c]})
    common = None
    unique = None
    for total in totals:
        if len(totals[total]) > 1:
            common = totals[total][0]
        else:
            unique = totals[total][0]
    return unique.weight + common.total() - unique.total()

def read(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        data = []
        lookup = {}
        for line in lines:
            d = line.split()
            key = d[0]
            weight = int(d[1].strip('(').strip(')'))
            children = []
            for c in d[3:]:
                children.append(c.strip(','))
            node = Node(key, weight, children)
            data.append(node)
            lookup.update({key: node})
        # second pass makes it a proper tree
        for node in data:
            children = []
            for key in node.children:
               children.append(lookup[key])
            node.children = children
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
