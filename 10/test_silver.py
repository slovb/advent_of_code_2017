import unittest
import silver as target

class Tester(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(target.calc(5, [3]), 2)
    def test_example_2(self):
        self.assertEqual(target.calc(5, [3, 4]), 12)
    def test_example_3(self):
        self.assertEqual(target.calc(5, [3, 4, 1]), 12)
    def test_example_4(self):
        self.assertEqual(target.calc(5, [3, 4, 1, 5]), 12)

if __name__ == '__main__':
    unittest.main()
