import unittest
import gold as target

class Tester(unittest.TestCase):
    def test_ex2(self):
        layers = {
            0: 3,
            1: 2,
            4: 4,
            6: 4
        }
        self.assertEqual(target.calc(layers), 10)
    def test_ex3(self):
        self.assertTrue(target.atZero(0, 3))
        self.assertFalse(target.atZero(1, 3))
        self.assertFalse(target.atZero(2, 3))
        self.assertFalse(target.atZero(3, 3))
        self.assertTrue(target.atZero(4, 3))
        self.assertFalse(target.atZero(5, 3))
        self.assertTrue(target.atZero(12, 3))
    def test_ex4(self):
        self.assertTrue(target.atZero(0, 2))
        self.assertFalse(target.atZero(1, 2))
        self.assertTrue(target.atZero(2, 2))
        self.assertFalse(target.atZero(3, 2))


if __name__ == '__main__':
    unittest.main()
