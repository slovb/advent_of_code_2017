def calc(dance, n, repeats):
    from string import ascii_lowercase
    order = ascii_lowercase[:n]
    memory = {}
    i = 0
    while i < repeats:
        memory.update({order: i})
        for move in dance:
            if move[0] == 's':
                order = spin(order, move)
            elif move[0] == 'x':
                order = exchange(order, move)
            elif move[0] == 'p':
                order = partner(order, move)
            else:
                raise Exception('What is "{}"?'.format(move))
        i += 1
        if order in memory:
            length = i - memory[order]
            while (i + length) < repeats:
                i += length
            memory = {} # clear memory to skip doing this again
    return order

def spin(order, move):
    size = int(move[1:])
    return order[-size:] + order[:-size]

def exchange(order, move):
    a = int(move[1:].split('/')[0])
    b = int(move.split('/')[1])
    return swap(order, a, b)

def partner(order, move):
    a = move[1:].split('/')[0]
    b = move.split('/')[1]
    i = order.index(a)
    j = order.index(b)
    return swap(order, i, j)

def swap(order, i, j):
    if i > j:
        i, j = j, i
    return order[:i] + order[j] + order[i+1:j] + order[i] + order[j+1:]

def read(filename):
    with open(filename, 'r') as f:
        return f.readline().split(',')

def main(filename):
    print calc(read(filename), 16, 10**9)

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
