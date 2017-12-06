import unittest
import gold as target

class Tester(unittest.TestCase):
    def test_example(self):
        self.assertEqual(target.calc([0, 2, 7, 0]), 4)

if __name__ == '__main__':
    unittest.main()
