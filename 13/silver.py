def calc(layers):
    depth = 0
    total = 0
    for i in range(max(layers) + 1):
        if i in layers:
            if pos(i, layers[i]) == depth:
                total += i * layers[i]
    return total

def pos(step, length):
    position = 0
    direction = 1
    for x in range(step):
        position += direction
        if position == length - 1:
            direction = -1
        elif position == 0:
            direction = 1
    return position

def read(filename):
    with open(filename, 'r') as f:
        layers = {}
        lines = f.readlines()
        for line in lines:
            parts = line.split(' ')
            key = int(parts[0].rstrip(':'))
            depth = int(parts[1])
            layers.update({key: depth})
        return layers

def main(filename):
    print calc(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
