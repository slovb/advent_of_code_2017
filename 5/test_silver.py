import unittest
import silver as target

class Tester(unittest.TestCase):
    def test_example(self):
        self.assertEqual(target.calc([0, 3, 0, 1, -3]), 5)

if __name__ == '__main__':
    unittest.main()
