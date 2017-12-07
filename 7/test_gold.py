import unittest
import gold as target

class Tester(unittest.TestCase):
    def test_example(self):
        example = []
        pbga = target.Node('pbga', 66)
        xhth = target.Node('xhth', 57)
        ebii = target.Node('ebii', 61)
        havc = target.Node('havc', 66)
        ktlj = target.Node('ktlj', 57)
        cntj = target.Node('cntj', 57)
        qoyq = target.Node('qoyq', 66)
        jptl = target.Node('jptl', 61)
        gyxo = target.Node('gyxo', 61)
        fwft = target.Node('fwft', 72, [ktlj, cntj, xhth])
        padx = target.Node('padx', 45, [pbga, havc, qoyq])
        ugml = target.Node('ugml', 68, [gyxo, ebii, jptl])
        tknk = target.Node('tknk', 41, [ugml, padx, fwft])
        self.assertEqual(target.calc(tknk), 60)

if __name__ == '__main__':
    unittest.main()
