class Condition:
    def __init__(self, key, comparison, value):
        self.key = key
        self.comparison = comparison
        self.value = value
    def isTrue(self, registers):
        value = registers[self.key]
        if self.comparison == '==':
            return value == self.value
        elif self.comparison == '>':
            return value > self.value
        elif self.comparison == '>=':
            return value >= self.value
        elif self.comparison == '<':
            return value < self.value
        elif self.comparison == '<=':
            return value <= self.value
        elif self.comparison == '!=':
            return value != self.value
        else:
            raise Exception('unknown comparison op: ' + self.comparison)

class Instruction:
    def __init__(self, key, op, value, condition):
        self.key = key
        self.op = op
        self.value = value
        self.condition = condition

def calc(instructions):
    registers = {}
    maximum = 0
    for instruction in instructions:
        # make sure a default exists
        if not instruction.key in registers:
            registers.update({instruction.key: 0})
        if not instruction.condition.key in registers:
            registers.update({instruction.condition.key: 0})
        if instruction.condition.isTrue(registers):
            if instruction.op == 'inc':
                registers[instruction.key] += instruction.value
            elif instruction.op == 'dec':
                registers[instruction.key] -= instruction.value
            else:
                raise Exception('unknown op: ' + instruction.op)
            if registers[instruction.key] > maximum:
                maximum = registers[instruction.key]
    return maximum

def parse(lines):
    instructions = []
    for line in lines:
        parts = line.split()
        key = parts[0]
        op = parts[1]
        value = int(parts[2])

        conditionKey = parts[4]
        conditionComparison = parts[5]
        conditionValue = int(parts[6])

        instructions.append(Instruction(key, op, value, Condition(
            conditionKey, conditionComparison, conditionValue)))
    return instructions

def read(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return parse(lines)

def main(filename):
    print calc(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
