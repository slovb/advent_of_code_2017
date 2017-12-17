def calc(steps, repeats = 5*(10**7)):
    pos = 0
    l = 1
    num = -1
    while l < repeats + 1:
        pos = (pos + steps) % l
        pos += 1 # insert ahead
        if pos == 1:
            num = l
        l += 1
    return num

def main(inp):
    print calc(int(inp))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for i in sys.argv[1:]:
        main(i)
