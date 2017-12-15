def calc(a, b, repeats):
    total = 0
    for i in range(repeats):
        a = genA(a)
        b = genB(b)
        if match(a, b):
            total += 1
    return total

def match(a, b):
    mod = 2**16
    return (a % mod) == (b % mod)

def genA(n):
    factor = 16807
    modulo = 2147483647
    test = 4
    return gen(n, factor, modulo, test)

def genB(n):
    factor = 48271
    modulo = 2147483647
    test = 8
    return gen(n, factor, modulo, test)
    
def gen(n, factor, modulo, test = 1):
    res = (n * factor) % modulo
    if (res % test == 0):
        return res
    return gen(res, factor, modulo, test)

def main(a, b):
    print calc(a, b, 5*10**6)

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 3):
        print('missing input parameter')
        exit()
    main(int(sys.argv[1]), int(sys.argv[2]))

