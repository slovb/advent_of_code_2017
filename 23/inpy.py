a = 1
b = 67
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0

b *= 100
b += 100000
c = b
c += 17000

while True:
    f = 1
    d = 2
    while d != b:
        e = 2
        while e != b:
            if d * e == b:
                f = 0
            e += 1
            print '{} {} {} {} {} {} {} {}'.format(a,b,c,d,e,f,g,h)
        d += 1
        print '{} {} {} {} {} {} {} {}'.format(a,b,c,d,e,f,g,h)
    if f == 0:
        h += 1
    print '{} {} {} {} {} {} {} {}'.format(a,b,c,d,e,f,g,h)
    if b == c:
        break
    else:
        b += 17
print h
