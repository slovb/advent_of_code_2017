def execute(program):
    pc = 0
    ref = 0
    snd = 0
    registry = {}
    while pc < len(program):
        i = program[pc]
        op = i[0]
        # get x
        x = i[1]
        if x not in registry:
            registry.update({x:0})
        # get y
        y = 0
        if len(i) == 3:
            y = i[2]
        # get vx
        vx = registry[x]
        # get vy
        vy = 0
        try:
            vy = int(y)
        except(ValueError, TypeError):
            vy = registry[y]
        # execute
        if op == 'snd':
            snd = vx
        elif op == 'rcv':
            if vx != 0:
                return snd
        elif op == 'jgz':
            if vx > 0:
                pc += vy - 1 # -1 to compensate for incrementation
        else:
            if op == 'set':
                vx = vy
            elif op == 'add':
                vx += vy
            elif op == 'mul':
                vx *= vy
            elif op == 'mod':
                vx %= vy
            else:
                raise Exception('Unknown op: {}'.format(op))
            registry.update({x:vx})
        # increment
        pc += 1

def read(filename):
    with open(filename, 'r') as f:
        return [r.split() for r in f.readlines()]

def main(filename):
    print execute(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
