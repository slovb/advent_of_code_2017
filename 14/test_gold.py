import unittest
import gold as target

class Tester(unittest.TestCase):
    def test_ex(self):
        self.assertEqual(target.calc('flqrgnkx'), 1242)

if __name__ == '__main__':
    unittest.main()

