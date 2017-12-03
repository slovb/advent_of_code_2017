import unittest
import silver

class TestSilver(unittest.TestCase):
    def test_1(self):
        self.assertEqual(silver.calc(1), 0)
    def test_12(self):
        self.assertEqual(silver.calc(12), 3)
    def test_23(self):
        self.assertEqual(silver.calc(23), 2)
    def test_1024(self):
        self.assertEqual(silver.calc(1024), 31)

if __name__ == '__main__':
    unittest.main()
