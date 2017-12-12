import unittest
import gold as target

class Tester(unittest.TestCase):
    def test_ex(self):
        adjacency = {
            0: [2],
            1: [1],
            2: [0, 3, 4],
            3: [2, 4],
            4: [2, 3, 6],
            5: [6],
            6: [4, 5]
        }
        self.assertEqual(target.calc(adjacency), 2)

if __name__ == '__main__':
    unittest.main()
