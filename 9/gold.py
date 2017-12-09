def purify(stream):
    import re
    stream = re.sub('!.', '', stream)
    return stream

def calc(stream):
    stream = purify(stream)
    k = 0
    inGarbage = False
    for ch in stream:
        if inGarbage:
            if ch == '>':
                inGarbage = False
            else:
                k += 1
        else:
            if ch == '<':
                inGarbage = True
    return k

def read(filename):
    with open(filename, 'r') as f:
        line = f.readline().rstrip()
        return line

def main(filename):
    print calc(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
