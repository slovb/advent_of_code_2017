import unittest
import silver as target

class Tester(unittest.TestCase):
    def test_ex(self):
        particles = [
            target.Particle(0, (3, 0, 0), (2, 0, 0), (-1, 0, 0)),
            target.Particle(1, (4, 0, 0), (0, 0, 0), (-2, 0, 0))
        ]
        self.assertEqual(target.calc(particles), 0)

if __name__ == '__main__':
    unittest.main()
