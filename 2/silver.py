def calc(data):
    checks = map(lambda x: max(x) - min(x), data)
    return sum(checks)

def main(filename):
    import reader
    print(calc(reader.readInt(filename)))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
