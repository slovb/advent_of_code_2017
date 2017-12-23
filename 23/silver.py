class CPU:
    def __init__(self):
        self.pc = 0
        self.registry = {}
        self.counter = 0
    def step(self, program):
        i = program[self.pc]
        op = i[0]
        # get x
        x = i[1]
        if x not in self.registry:
            self.registry.update({x:0})
        # get y
        y = 0
        if len(i) == 3:
            y = i[2]
        # get vx
        try:
            vx = int(x)
        except(ValueError, TypeError):
            vx = self.registry[x]
        # get vy
        try:
            vy = int(y)
        except(ValueError, TypeError):
            vy = self.registry[y]
        # execute
        if op == 'jnz':
            if vx != 0:
                self.pc += vy - 1 # -1 to compensate for incrementation
        else:
            if op == 'set':
                vx = vy
            elif op == 'sub':
                vx -= vy
            elif op == 'mul':
                vx *= vy
                self.counter += 1
            else:
                raise Exception('Unknown op: {}'.format(op))
            self.registry.update({x:vx})
        # increment
        self.pc += 1
        return True

def execute(program):
    cpu = CPU()
    while cpu.pc < len(program):
        cpu.step(program)
    return cpu.counter

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
