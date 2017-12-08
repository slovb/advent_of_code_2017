import unittest
import gold as target

class Tester(unittest.TestCase):
    def test_example(self):
        lines = [
            'b inc 5 if a > 1',
            'a inc 1 if b < 5',
            'c dec -10 if a >= 1',
            'c inc -20 if c == 10'
        ]
        self.assertEqual(target.calc(target.parse(lines)), 10)

if __name__ == '__main__':
    unittest.main()
