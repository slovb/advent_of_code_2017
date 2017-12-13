def calc(layers):
    delay = 0
    solved = isSolution(layers, delay)
    while not solved:
        delay += 1
        solved = isSolution(layers, delay)
    return delay

def isSolution(layers, delay):
    total = 0
    for i in range(max(layers) + 1):
        if i in layers:
            time = i + delay
            if atZero(time, layers[i]):
                if time > 0:
                    return False
    return True

def atZero(time, length):
    if time % (2 * length - 2) == 0:
        return True
    return False

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
