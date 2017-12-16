def calc(dance, n):
    from string import ascii_lowercase
    lst = [c for c in ascii_lowercase[:n]]
    for move in dance:
        if move[0] == 's':
            lst = spin(lst, move)
        elif move[0] == 'x':
            lst = exchange(lst, move)
        elif move[0] == 'p':
            lst = partner(lst, move)
        else:
            raise Exception('What is "{}"?'.format(move))
    return ''.join(lst)

def spin(lst, move):
    size = int(move[1:])
    for i in range(size):
        lst.insert(0, lst.pop())
    return lst

def exchange(lst, move):
    a = int(move[1:].split('/')[0])
    b = int(move.split('/')[1])
    lst[a], lst[b] = lst[b], lst[a]
    return lst

def partner(lst, move):
    a = move[1:].split('/')[0]
    b = move.split('/')[1]
    i = lst.index(a)
    j = lst.index(b)
    lst[i], lst[j] = lst[j], lst[i]
    return lst

def read(filename):
    with open(filename, 'r') as f:
        return f.readline().split(',')

def main(filename):
    print calc(read(filename), 16)

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
