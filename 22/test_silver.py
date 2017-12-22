import unittest
import silver as target

class Tester(unittest.TestCase):
    def test_ex(self):
        from sets import Set
        initial = Set()
        initial.add((-1, 0))
        initial.add((1, 1))
        self.assertEqual(target.calc(initial, 0, True), 0)
        self.assertEqual(target.calc(initial, 1, True), 1)
        self.assertEqual(target.calc(initial, 2, True), 1)
        self.assertEqual(target.calc(initial, 7, True), 5)
        self.assertEqual(target.calc(initial, 70, True), 41)
        self.assertEqual(target.calc(initial, 10**4), 5587)

if __name__ == '__main__':
    unittest.main()
