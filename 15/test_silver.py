import unittest
import silver as target

class Tester(unittest.TestCase):
    def test_ex_a(self):
        values = [
            65,
            1092455,
            1181022009,
            245556042,
            1744312007,
            1352636452
        ]
        for i, n in enumerate(values[:-1]):
            self.assertEqual(target.genA(n), values[i+1])
    def test_ex_b(self):
        values = [
            8921,
            430625591,
            1233683848,
            1431495498,
            137874439,
            285222916
        ]
        for i, n in enumerate(values[:-1]):
            self.assertEqual(target.genB(n), values[i+1])
    def test_match(self):
        a = [
            1092455,
            1181022009,
            245556042,
            1744312007,
            1352636452
        ]
        b = [
            430625591,
            1233683848,
            1431495498,
            137874439,
            285222916
        ]
        m = [
            False,
            False,
            True,
            False,
            False
        ]
        for i in range(len(a)):
            self.assertEqual(target.match(a[i], b[i]), m[i])
    def test_ex(self):
        self.assertEqual(target.calc(65, 8921, 4*10**7), 588)

if __name__ == '__main__':
    unittest.main()
