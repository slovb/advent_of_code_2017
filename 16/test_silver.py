import unittest
import silver as target

class Tester(unittest.TestCase):
    def test_ex(self):
        dance = ['s1', 'x3/4', 'pe/b']
        self.assertEqual(target.calc(dance, 5), 'baedc')

if __name__ == '__main__':
    unittest.main()
