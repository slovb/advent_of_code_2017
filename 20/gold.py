class Particle:
    def __init__(self, i, p, v, a):
        self.id = i
        self.p = p
        self.v = v
        self.a = a
        self.d = len(p)

    def simulate(self):
        v = tuple([self.v[i] + self.a[i] for i in range(self.d)])
        self.v = v
        p = tuple([self.p[i] + self.v[i] for i in range(self.d)])
        self.p = p

    def distance(self):
        return sum([abs(self.p[i]) for i in range(self.d)])

def calc(particles):
    from sets import Set
    limit = 1000
    accidentFree = 0
    while accidentFree < limit:
        positions = Set()
        collisions = []
        for particle in particles:
            particle.simulate()
            if particle.p in positions:
                collisions.append(particle.p)
            else:
                positions.add(particle.p)

        # prune collisions
        remove = []
        for i, particle in enumerate(particles):
            if particle.p in collisions:
                remove.append(i)
        for i in remove[::-1]:
            particles.pop(i)

        # manage counter
        if len(collisions) == 0:
            accidentFree += 1
        else:
            accidentFree = 0
    return len(particles)


def read(filename):
    def splint(v):
        return tuple([int(c) for c in v.split(',')])
    import re
    extract = re.compile('p=<(?P<p>.+)>, v=<(?P<v>.+)>, a=<(?P<a>.+)>')
    particles = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            parts = re.match(extract, line).groupdict()
            p = splint(parts['p'])
            v = splint(parts['v'])
            a = splint(parts['a'])
            particles.append(Particle(i, p, v, a))
    return particles

def main(filename):
    print calc(read(filename))

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
