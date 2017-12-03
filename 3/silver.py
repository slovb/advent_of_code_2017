def calc(n):
    i = 0 # coordinate i
    j = 0 # coordinate j
    d = 0 # direction: right, up, left, down
    displacement = {
        0: [1, 0],
        1: [0, 1],
        2: [-1, 0],
        3: [0, -1]
    }
    s = 1 # number of steps between turns
    c = 0 # count the steps taken in current directions
    for x in range(n - 1): # repeat n-1 times
        i += displacement[d][0]
        j += displacement[d][1]
        c = (c + 1) % s
        if c == 0: # time to turn
            d = (d + 1) % 4
            if d % 2 == 0: # left or right -> increase num steps
                s += 1
    return abs(i) + abs(j)

def main(n):
    print calc(n)

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for n in sys.argv[1:]:
        main(int(n))
