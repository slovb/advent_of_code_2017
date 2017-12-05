import unittest
import gold as target

class TestGold(unittest.TestCase):
    def test_silver_example(self):
        self.assertTrue(target.test('aa bb cc dd ee'))
        self.assertFalse(target.test('aa bb cc dd aa'))
        self.assertTrue(target.test('aa bb cc dd aaa'))

    def test_gold_example(self):
        self.assertTrue(target.test('abcde fghij'))
        self.assertFalse(target.test('abcde xyz ecdab'))
        self.assertTrue(target.test('a ab abc abd abf abj'))
        self.assertTrue(target.test('iiii oiii ooii oooi oooo'))
        self.assertFalse(target.test('oiii ioii iioi iiio'))

if __name__ == '__main__':
    unittest.main()
