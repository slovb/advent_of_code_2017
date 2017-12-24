import unittest
import gold as target

class Tester(unittest.TestCase):
    def test_ex(self):
        components = [
            (0, 2),
            (2, 2),
            (2, 3),
            (3, 4),
            (3, 5),
            (0, 1),
            (10, 1),
            (9, 10)
        ]
        self.assertEqual(target.solve(components), 19)

if __name__ == '__main__':
    unittest.main()
