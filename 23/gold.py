class CPU:
    def __init__(self):
        self.pc = 0
        self.registry = {
            'a': 1,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0,
            'g': 0,
            'h': 0
        }
    def step(self, program):
        i = program[self.pc]
        op = i[0]
        # get x
        x = i[1]
        if x == 'nop':
            self.pc += 1
            return True
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
            else:
                raise Exception('Unknown op: {}'.format(op))
            self.registry.update({x:vx})
        # increment
        self.pc += 1
        return True
    def __str__(self):
        reg = []
        for k, v in self.registry.items():
            reg.append('{}: {}'.format(k, v))
        return '{}; '.format(self.pc) + ', '.join(reg)

def execute(program):
    cpu = CPU()
    while cpu.pc < len(program):
        cpu.step(program)
        print cpu
    return cpu.registry['h']

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
