class Grid:
    def __init__(self):
        self.state = '.#./..#/###'

    def enhance(self, ruleset):
        cellSize = None
        if self.size() % 2 == 0:
            cellSize = 2
        elif self.size() % 3 == 0:
            cellSize = 3
        else:
            raise Exception('Size issues')
        cellsPerRow = self.size() / cellSize
        cells = self.split(cellsPerRow, cellSize)
        enhanced = []
        for cell in cells:
            enhanced.append(ruleset[cell])
        cellSize += 1
        self.state = self.merge(enhanced, cellsPerRow, cellSize)

    def split(self, cellsPerRow, cellSize):
        matrix = explode(self.state)
        cells = [] 
        for y in range(cellsPerRow):
            oy = y * cellSize # offset y
            for x in range(cellsPerRow):
                ox = x * cellSize # offset x
                cell = []
                for j in range(cellSize): # local y
                    row = []
                    for i in range(cellSize): # local x
                        row.append(matrix[oy + j][ox + i])
                    cell.append(row)
                cells.append(implode(cell))
        return cells

    def merge(self, cells, cellsPerRow, cellSize):
        width = cellsPerRow * cellSize
        state = [['.']*width for i in range(width)] # width X width '.' matrix
        for y in range(len(state)):
            cy = y / cellSize # cell y
            for x in range(len(state)):
                cx = x / cellSize # cell x
                cell = cells[cx + cy * cellsPerRow]
                i = x % cellSize # local x
                j = y % cellSize # local y
                pos = i + j * (cellSize + 1) # + 1 to skip every /
                if (cell[pos] == '#'):
                    state[y][x] = '#'
        return implode(state)

    def count(self):
        return self.state.count('#')

    def size(self):
        return self.state.count('/') + 1

    def __str__(self):
        return '\n'.join(self.state.split('/'))

def calc(ruleset, iterations):
    grid = Grid()
    for i in range(iterations):
        grid.enhance(ruleset)
    return grid.count()

def explode(text):
    rows = text.split('/')
    matrix = []
    for row in rows:
        matrix.append([c for c in row])
    return matrix 

def implode(matrix):
    rows = [''.join(row) for row in matrix]
    return '/'.join(rows)

def read(filename):
    def rotate(matrix):
        d = len(matrix)
        rot = [['.'] * d for i in range(d)] # d*d square . matrix
        for y in range(d):
            for x in range(d):
                rotX = d - y - 1
                rotY = x
                rot[rotY][rotX] = matrix[y][x]
        return rot

    def flipVertical(matrix):
        return matrix[::-1]

    def updateWithSymmetries(ruleset, key, val):
        def up(ruleset, keyMatrix, val):
            key = implode(keyMatrix)
            if key in ruleset:
                if ruleset[key] != val:
                    raise Exception('Problematic symmetries')
            ruleset.update({key: val})
        mn = explode(key)
        mf = flipVertical(mn)
        up(ruleset, mn, val)
        up(ruleset, mf, val)
        for i in range(3):
            mn = rotate(mn)
            mf = rotate(mf)
            up(ruleset, mn, val)
            up(ruleset, mf, val)

    import re
    extract = re.compile('(?P<key>[.#/]+) => (?P<val>[.#/]+)')
    ruleset = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            rule = re.match(extract, line).groupdict()
            key = rule['key']
            val = rule['val']
            updateWithSymmetries(ruleset, key, val)
    return ruleset

def main(filename, iterations):
    print calc(read(filename), int(iterations))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 3):
        print('missing input parameter')
        exit()
    main(sys.argv[1], sys.argv[2])
