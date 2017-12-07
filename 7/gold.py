class Node:
    def __init__(self, key, weight, children = []):
        self.key = key
        self.weight = weight
        self.children = children
    def __str__(self):
        children = []
        for c in self.children:
            children.append(c.key)
        return "{} {}/{}: {}".format(
            self.key,
            self.weight,
            self.total(),
            ', '.join(children)
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

def findUnbalance(node):
    # abuse that we know only one branch is inbalanced
    for c in node.children:
        if not c.isBalanced():
            return findUnbalance(c)
    return node

def calc(root):
    node = findUnbalance(root)
    # figure out how to balance 
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
        nodes = []
        for line in lines:
            d = line.split()
            key = d[0]
            weight = int(d[1].strip('(').strip(')'))
            children = []
            for c in d[3:]:
                children.append(c.strip(','))
            nodes.append({'key': key, 'weight': weight, 'children': children})
        reference = {}
        node = None
        # add any node whose children already exists
        while len(nodes) > 0:
            i = len(nodes) - 1
            # loop backwards so we can pop the list as we go
            while i >= 0:
                incomplete = False
                for c in nodes[i]['children']:
                    if not c in reference:
                        incomplete = True # missing children
                        break
                if not incomplete:
                    key = nodes[i]['key']
                    weight = nodes[i]['weight']
                    children = []
                    for ckey in nodes[i]['children']:
                        children.append(reference[ckey])
                    node = Node(key, weight, children)
                    reference.update({key: node})
                    nodes.pop(i) # note removal
                i -= 1
        return node

def main(filename):
    print calc(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
