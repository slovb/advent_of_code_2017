def get(lab, x, y):
    xLim = len(lab[0])
    yLim = len(lab)
    if x > xLim or x < 0:
        return ' '
    if y > yLim or y < 0:
        return ' '
    return lab[y][x]

def run(lab):
    x, y = findStart(lab)
    d = initialDirection(lab, x, y)
    cur = get(lab, x, y)
    counter = 0
    while cur != ' ':
        # check
        if cur == '+':
            yInc = get(lab, x, y + 1)
            yDec = get(lab, x, y - 1)
            xInc = get(lab, x + 1, y)
            xDec = get(lab, x - 1, y)
            if d % 2 == 0:
                if xInc != ' ' and xInc != '|':
                    d = 1
                elif xDec != ' ' and xDec != '|':
                    d = 3
            else:
                if yInc != ' ' and yInc != '-':
                    d = 0
                elif yDec != ' ' and yDec != '-':
                    d = 2

        # step
        if d == 0:
            y += 1
        elif d == 1:
            x += 1
        elif d == 2:
            y -= 1
        elif d == 3:
            x -= 1
        counter += 1

        # update
        cur = get(lab, x, y)
    return counter

def findStart(lab):
    xLim = len(lab[0])
    yLim = len(lab)
    def test(lab, x, y):
        return get(lab, x, y) != ' '

    for x in range(xLim):
        if test(lab, x, 0):
            return (x, 0)
        elif test(lab, x, yLim - 1):
            return (x, yLim - 1)
    for y in range(yLim):
        if test(lab, 0, y):
            return (0, y)
        elif test(lab, xLim - 1, y):
            return (xLim - 1, y)
    raise Exception('Could not find start')

def initialDirection(lab, x, y):
    d = (0, 0)
    if (lab[y][x] == '|'):
        if (y == 0):
            d = 0
        else:
            d = 2
    else:
        if (x == 0):
            d = 1
        else:
            d = 3
    return d

def read(filename):
    with open(filename, 'r') as f:
        return [l.rstrip("\n") for l in f.readlines()]

def main(filename):
    print run(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
