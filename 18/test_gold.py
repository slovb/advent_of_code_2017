import unittest
import gold as target

class Tester(unittest.TestCase):
    def test_ex(self):
        program = [
			"snd 1",
			"snd 2",
			"snd p",
			"rcv a",
			"rcv b",
			"rcv c",
			"rcv d"
        ]
        program = [instruction.split() for instruction in program]
        self.assertEqual(target.execute(program), 3)

if __name__ == '__main__':
    unittest.main()
