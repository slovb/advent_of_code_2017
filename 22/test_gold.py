import unittest
import gold as target

class Tester(unittest.TestCase):
    def test_ex(self):
        from sets import Set
        initial = Set()
        initial.add((-1, 0))
        initial.add((1, 1))
        self.assertEqual(target.calc(initial, 0, True), 0)
        self.assertEqual(target.calc(initial, 1, True), 0)
        self.assertEqual(target.calc(initial, 2, True), 0)
        self.assertEqual(target.calc(initial, 6, True), 0)
        self.assertEqual(target.calc(initial, 7, True), 1)
        self.assertEqual(target.calc(initial, 100, True), 26)
        self.assertEqual(target.calc(initial, 10**7), 2511944)

if __name__ == '__main__':
    unittest.main()
