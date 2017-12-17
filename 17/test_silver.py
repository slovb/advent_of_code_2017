import unittest
import silver as target

class Tester(unittest.TestCase):
    def test_ex(self):
        self.assertEqual(target.calc(3), 638)
    def test_ex2(self):
        self.assertEqual(target.calc(3, 3), 1)
    def test_ex3(self):
        self.assertEqual(target.calc(3, 4), 3)
    def test_ex4(self):
        self.assertEqual(target.calc(3, 5), 2)
    def test_ex5(self):
        self.assertEqual(target.calc(3, 6), 1)
    def test_ex6(self):
        self.assertEqual(target.calc(3, 7), 2)
    def test_ex7(self):
        self.assertEqual(target.calc(3, 8), 6)
    def test_ex8(self):
        self.assertEqual(target.calc(3, 9), 5)

if __name__ == '__main__':
    unittest.main()
