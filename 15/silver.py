def calc(a, b, repeats):
    total = 0
    for i in range(repeats):
        a = genA(a)
        b = genB(b)
        if match(a, b):
            total += 1
    return total

def tail(n):
    return '{0:16b}'.format(n)

def match(a, b):
    #return tail(a) == tail(b)
    return (b - a) % (2**16) == 0

def genA(n):
    factor = 16807
    modulo = 2147483647
    return gen(n, factor, modulo)

def genB(n):
    factor = 48271
    modulo = 2147483647
    return gen(n, factor, modulo)
    
def gen(n, factor, modulo):
    return (n * factor) % modulo

def main(a, b):
    print calc(a, b, 4*10**7)

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 3):
        print('missing input parameter')
        exit()
    main(int(sys.argv[1]), int(sys.argv[2]))

