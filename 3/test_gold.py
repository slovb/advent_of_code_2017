import unittest
import gold

class TestSilver(unittest.TestCase):
    def test_0(self):
        self.assertEqual(gold.calc(0), 1)
    def test_1(self):
        self.assertEqual(gold.calc(1), 2)
    def test_2(self):
        self.assertEqual(gold.calc(2), 4)
    def test_3(self):
        self.assertEqual(gold.calc(3), 4)
    def test_4(self):
        self.assertEqual(gold.calc(4), 5)
    def test_9(self):
        self.assertEqual(gold.calc(9), 10)
    def test_10(self):
        self.assertEqual(gold.calc(10), 11)
    def test_140(self):
        self.assertEqual(gold.calc(140), 142)
    def test_800(self):
        self.assertEqual(gold.calc(800), 806)

if __name__ == '__main__':
    unittest.main()

