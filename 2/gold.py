def main(filename):
    def calc(data):
        sum = 0
        for row in data:
            row.sort()
            for i, x in enumerate(row):
                for j, y in enumerate(row[i+1:]):
                    if y % x == 0:
                        sum += y / x
        return sum
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
