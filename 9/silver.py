def purify(stream):
    import re
    stream = re.sub('!.', '', stream)
    stream = re.sub('<[^>]*>', '', stream)
    stream = re.sub('[^{}]', '', stream)
    return stream

def calc(stream):
    stream = purify(stream)
    def parser(stream, point = 0, i = 0):
        value = point
        while True:
            if i >= len(stream):
                break
            if stream[i] == '}':
                break
            elif stream[i] == '{': 
                i, v = parser(stream, point + 1, i + 1)
                value += v
            i += 1
        return (i, value)
    return parser(stream)[1]

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
