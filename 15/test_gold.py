import unittest
import gold as target

class Tester(unittest.TestCase):
    def test_ex_a(self):
        values = [
            65,
            1352636452,
            1992081072,
            530830436,
            1980017072,
            740335192 
        ]
        for i, n in enumerate(values[:-1]):
            self.assertEqual(target.genA(n), values[i+1])
    def test_ex_b(self):
        values = [
            8921, 
            1233683848,
            862516352,
            1159784568,
            1616057672, 
            412269392
        ]
        for i, n in enumerate(values[:-1]):
            self.assertEqual(target.genB(n), values[i+1])
    def test_match(self):
        a = [
            1352636452,
            1992081072,
            530830436,
            1980017072,
            740335192
        ]
        b = [
            1233683848,
            862516352,
            1159784568,
            1616057672, 
            412269392
        ]
        m = [
            False,
            False,
            False,
            False,
            False,
        ]
        for i in range(len(a)):
            self.assertEqual(target.match(a[i], b[i]), m[i])
        self.assertEqual(target.match(1023762912, 896885216), True)
    def test_ex(self):
        self.assertEqual(target.calc(65, 8921, 5*10**6), 309)
        pass

if __name__ == '__main__':
    unittest.main()
