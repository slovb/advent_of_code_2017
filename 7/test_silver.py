import unittest
import silver as target

class Tester(unittest.TestCase):
    def test_example(self):
        example = []
        example.append(target.Node('pbga', 66))
        example.append(target.Node('xhth', 57))
        example.append(target.Node('ebii', 61))
        example.append(target.Node('havc', 66))
        example.append(target.Node('ktlj', 57))
        example.append(target.Node('fwft', 72, ['ktlj', 'cntj', 'xhth']))
        example.append(target.Node('qoyq', 66))
        example.append(target.Node('padx', 45, ['pbga', 'havc', 'qoyq']))
        example.append(target.Node('tknk', 41, ['ugml', 'padx', 'fwft']))
        example.append(target.Node('jptl', 61))
        example.append(target.Node('ugml', 68, ['gyxo', 'ebii', 'jptl']))
        example.append(target.Node('gyxo', 61))
        example.append(target.Node('cntj', 57))
        self.assertEqual(target.calc(example), 'tknk')

if __name__ == '__main__':
    unittest.main()
