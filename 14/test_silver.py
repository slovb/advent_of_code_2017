import unittest
import silver as target

class Tester(unittest.TestCase):
    def test_ex(self):
        self.assertEqual(target.calc('flqrgnkx'), 8108)

if __name__ == '__main__':
    unittest.main()

