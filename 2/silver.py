def main(filename):
    def calc(data):
        checks = map(lambda x: max(x) - min(x), data)
        return sum(checks)
    with open(filename, 'r') as f:
        data = []
        for line in f:
            data.append(map(int, line.split()))
        print(calc(data))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
