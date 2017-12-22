def calc(infected, iterations, debug = False):
    from sets import Set
    infected = infected.copy() # copy to be safe
    d = 0 # 0 = up, 1 = right, 2 = down, 3 = left
    x = 0
    y = 0
    infections = 0
    for i in range(iterations):
        pos = (x, y)

        # turn & flip
        if pos in infected:
            d = (d + 1) % 4
            infected.remove(pos)
        else:
            d = (d - 1) % 4
            infected.add(pos)
            infections += 1

        # step forward
        if d == 0:
            y += 1
        elif d == 1:
            x += 1
        elif d == 2:
            y -= 1
        elif d == 3:
            x -= 1
        else:
            raise Exception('Unbound direction')
    if debug:
        print visualize((x, y), infected)
        print ' '
    return infections

def visualize(pos, infected):
    radius = 10
    vis = []
    for y in range(radius, -radius, -1):
        row = []
        for x in range(-radius, radius):
            p = (x, y)
            if p in infected:
                if p != pos:
                    row.append('#')
                else:
                    row.append('@')
            else:
                if p != pos:
                    row.append('.')
                else:
                    row.append('!')
        vis.append(' '.join(row))
    output = '\n'.join(vis)
    output = output.replace(' ! ', '[.]')
    output = output.replace(' @ ', '[#]')
    return output

def read(filename):
    from sets import Set
    initial = Set()
    with open(filename, 'r') as f:
        lines = f.readlines()
        hx = (len(lines[0]) - 1) // 2
        hy = len(lines) // 2
        for j, line in enumerate(lines):
            for i in range(len(line)):
                if line[i] == '#':
                    x = i - hx
                    y = hy - j
                    initial.add((x, y))
    return initial

def main(filename, iterations):
    print calc(read(filename), int(iterations))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 3):
        print('missing input parameter')
        exit()
    main(sys.argv[1], sys.argv[2])
