class Tape:
    def __init__(self, state):
        self.internal = {}
        self.id = 0
        self.state = state

    def get(self, i = None):
        if i == None:
            i = self.id
        if i in self.internal:
            return self.internal[i]
        return 0

    def execute(self, instructions):
        instruction = instructions[self.state][self.get()]
        self.set(instruction['write'])
        if (instruction['move'] == 'left'):
            self.left()
        elif (instruction['move'] == 'right'):
            self.right()
        else:
            raise Exception('unknown move')
        self.state = instruction['continue']
        return self

    def set(self, val):
        self.internal.update({self.id: val})
        return self

    def right(self):
        self.id += 1
        return self

    def left(self):
        self.id -= 1
        return self

    def count(self):
        c = 0
        for k in self.internal:
            if self.internal[k] == 1:
                c += 1
        return c

def solve(instructions):
    tape = Tape(instructions['begin'])
    for i in range(instructions['steps']):
        tape.execute(instructions)
    return tape.count()

def read(filename):
    with open(filename, 'r') as f:
        lines = [l.rstrip().rstrip('.').rstrip(':').split() for l in f.readlines()]
        instructions = {}
        instructions.update({'begin': lines[0][3]})
        instructions.update({'steps': int(lines[1][5])})
        i = 3
        while i < len(lines):
            instruction = {
                0: {
                    'write': int(lines[i + 2][4]),
                    'move': lines[i + 3][6],
                    'continue': lines[i + 4][4]
                },
                1: {
                    'write': int(lines[i + 6][4]),
                    'move': lines[i + 7][6],
                    'continue': lines[i + 8][4]
                }
            }
            instructions.update({lines[i][2]: instruction})
            i += 10
        return instructions

def main(filename):
    print solve(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print 'missing input parameter'
        exit()
    for f in sys.argv[1:]:
        main(f)
