import unittest
import silver as target

class Tester(unittest.TestCase):
    def test_ex(self):
        instructions = {
            'begin': 'A',
            'steps': 6,
            'A': { 
                0: {
                    'write': 1,
                    'move': 'right',
                    'continue': 'B'
                },
                1: {
                    'write': 0,
                    'move': 'left',
                    'continue': 'B'
                }
            },
            'B': {
                0: {
                    'write': 1,
                    'move': 'left',
                    'continue': 'A'
                },
                1: {
                    'write': 1,
                    'move': 'right',
                    'continue': 'A'
                }
            }
        }
        self.assertEqual(target.solve(instructions), 3)

if __name__ == '__main__':
    unittest.main()

