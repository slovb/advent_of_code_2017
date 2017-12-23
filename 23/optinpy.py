b = 106700
c = b + 17000
isPrime = False
h = 0

while True:
    isPrime = True
    d = 2
    while d < b:
        if b % d == 0:
            isPrime = False
            break
        """
        e = d
        while e != b:
            if d * e == b:
                isPrime = False
            e += 1
        """
        d += 1
    if isPrime == False:
        h += 1
    print '{} {} {} {}'.format(b,c,isPrime,h)
    if b == c:
        break
    else:
        b += 17
print h
