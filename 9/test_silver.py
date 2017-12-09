import unittest
import silver as target

class Tester(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(target.calc('{}'), 1)
    def test_example_2(self):
        self.assertEqual(target.calc('{{{}}}'), 6)
    def test_example_3(self):
        self.assertEqual(target.calc('{{}{}}'), 5)
    def test_example_4(self):
        self.assertEqual(target.calc('{{{},{},{{}}}}'), 16)
    def test_example_5(self):
        self.assertEqual(target.calc('{<a>,<a>,<a>,<a>}'), 1)
    def test_example_6(self):
        self.assertEqual(target.calc('{{<ab>},{<ab>},{<ab>},{<ab>}}'), 9)
    def test_example_7(self):
        self.assertEqual(target.calc('{{<!!>},{<!!>},{<!!>},{<!!>}}'), 9)
    def test_example_8(self):
        self.assertEqual(target.calc('{{<a!>},{<a!>},{<a!>},{<ab>}}'), 3)
    def test_1(self):
        self.assertEqual(target.calc('{!!!!!}}'), 1)

if __name__ == '__main__':
    unittest.main()

