def readInt(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(map(int, line.split()))
    return data
