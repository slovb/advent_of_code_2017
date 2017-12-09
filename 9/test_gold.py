import unittest
import gold as target

class Tester(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(target.calc('<>'), 0)
    def test_example_2(self):
        self.assertEqual(target.calc('<random characters>'), 17)
    def test_example_3(self):
        self.assertEqual(target.calc('<<<<>'), 3)
    def test_example_4(self):
        self.assertEqual(target.calc('<{!>}>'), 2)
    def test_example_5(self):
        self.assertEqual(target.calc('<!!>'), 0)
    def test_example_6(self):
        self.assertEqual(target.calc('<{o"i!a,<{i<a>'), 10)

if __name__ == '__main__':
    unittest.main()

