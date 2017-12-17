def calc(steps, repeats = 2017):
    pos = 0
    buf = [0]
    for i in range(1, repeats + 1):
        pos = (pos + steps) % len(buf)
        pos += 1 # insert ahead
        buf.insert(pos, i)
    pos = (pos + 1) % len(buf)
    return buf[pos]

def main(inp):
    print calc(int(inp))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for i in sys.argv[1:]:
        main(i)
