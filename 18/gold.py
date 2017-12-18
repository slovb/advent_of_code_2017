class State:
    def __init__(self, pid):
        self.pid = pid
        self.pc = 0
        self.snd = []
        self.registry = {'p': pid}
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
        if op == 'snd':
            self.snd.append(vx)
            self.counter += 1
        elif op == 'rcv':
            if self.friend.hasMessage():
                vx = self.friend.pop()
                self.registry.update({x:vx})
            else:
                return False
        elif op == 'jgz':
            if vx > 0:
                self.pc += vy - 1 # -1 to compensate for incrementation
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
            self.registry.update({x:vx})
        # increment
        self.pc += 1
        return True
    def hasMessage(self):
        return len(self.snd) > 0
    def pop(self):
        out = self.snd[0]
        self.snd = self.snd[1:]
        return out

def execute(program):
    s0 = State(0)
    s1 = State(1)
    s0.friend = s1
    s1.friend = s0
    r0 = True
    r1 = True
    while r0 or r1:
        r0 = s0.step(program)
        r1 = s1.step(program)
    return s1.counter

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
