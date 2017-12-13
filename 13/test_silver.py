import unittest
import silver as target

class Tester(unittest.TestCase):
    def test_ex(self):
        layers = {
            0: 3,
            1: 2,
            4: 4,
            6: 4
        }
        self.assertEqual(target.calc(layers), 24)

if __name__ == '__main__':
    unittest.main()
