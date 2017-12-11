import unittest
import gold as target

class Tester(unittest.TestCase):
    def test_ex_1(self):
        self.assertEqual(target.calc(['ne','ne','ne']), 3)
    def test_ex_2(self):
        self.assertEqual(target.calc(['ne','ne','sw', 'sw']), 2)
    def test_ex_3(self):
        self.assertEqual(target.calc(['ne','ne','s', 's']), 2)
    def test_ex_4(self):
        self.assertEqual(target.calc(['se','sw','se', 'sw', 'sw']), 3)

if __name__ == '__main__':
    unittest.main()
