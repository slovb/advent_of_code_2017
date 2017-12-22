def calc(initial, iterations, debug = False):
    state = {}
    states = 4 # 0 = clean, 1 = weakend, 2 = infected, 3 = flagged
    for infected in initial:
        state.update({infected: 2})

    d = 0
    directions = 4 # 0 = up, 1 = right, 2 = down, 3 = left

    x = 0
    y = 0

    infections = 0
    for i in range(iterations):
        pos = (x, y)
        if pos not in state:
            state.update({pos: 0})

        # rotate
        s = state[pos]
        if s == 0:
            d = (d - 1) % directions
        elif s == 1:
            pass
        elif s == 2:
            d = (d + 1) % directions
        elif s == 3:
            d = (d + 2) % directions
        else:
            raise Exception('Unbound state')
        
        # flip
        state[pos] = (state[pos] + 1) % states
        if state[pos] == 2:
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
        print visualize((x, y), state)
        print ' '
    return infections

def visualize(pos, state):
    radius = 10
    vis = []
    for y in range(radius, -radius, -1):
        row = []
        for x in range(-radius, radius):
            p = (x, y)
            if p not in state:
                if p == pos:
                    row.append('!')
                else:
                    row.append('.')
            elif p == pos:
                marker = ['!', 'w', '@', 'f']
                row.append(marker[state[p]])
            else:
                marker = ['.', 'W', '#', 'F']
                row.append(marker[state[p]])
        vis.append(' '.join(row))
    output = '\n'.join(vis)
    output = output.replace(' ! ', '[.]')
    output = output.replace(' w ', '[W]')
    output = output.replace(' @ ', '[#]')
    output = output.replace(' f ', '[F]')
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
