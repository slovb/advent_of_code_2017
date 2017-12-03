def calc(data):
    sum = 0
    for row in data:
        row.sort()
        for i, x in enumerate(row):
            for j, y in enumerate(row[i+1:]):
                if y % x == 0:
                    sum += y / x
    return sum

def main(filename):
    import reader
    print calc(reader.readInt(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
