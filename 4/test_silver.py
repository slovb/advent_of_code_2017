import unittest
import silver as target

class TestSilver(unittest.TestCase):
    def test_example(self):
        self.assertTrue(target.test('aa bb cc dd ee'))
        self.assertFalse(target.test('aa bb cc dd aa'))
        self.assertTrue(target.test('aa bb cc dd aaa'))

if __name__ == '__main__':
    unittest.main()
