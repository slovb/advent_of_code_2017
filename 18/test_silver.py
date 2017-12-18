import unittest
import silver as target

class Tester(unittest.TestCase):
    def test_ex(self):
        program = [
            "set a 1",
            "add a 2",
            "mul a a",
            "mod a 5",
            "snd a",
            "set a 0",
            "rcv a",
            "jgz a -1",
            "set a 1",
            "jgz a -2"
        ]
        program = [instruction.split() for instruction in program]
        self.assertEqual(target.execute(program), 4)

if __name__ == '__main__':
    unittest.main()
