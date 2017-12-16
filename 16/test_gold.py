import unittest
import gold as target

class Tester(unittest.TestCase):
    def test_ex(self):
        dance = ['s1', 'x3/4', 'pe/b']
        self.assertEqual(target.calc(dance, 5, 1), 'baedc')
        self.assertEqual(target.calc(dance, 5, 2), 'ceadb')
    def test_2(self):
        dance = ['s1', 'x3/4', 'pe/b']
        self.assertEqual(target.calc(dance, 16, 2001), 'klmdnopaecbfghij')
    def test_3(self):
        dance = \
        's10,x5/9,s15,x3/4,s8,x15/0,s4,x6/11,pl/e,x15/10,s10,x2/8,s1,x15/0,s12,pa/o,x9/8,pi/f,s1,x6/5,s1,x3/9,pl/n,x4/8,pg/a,x10/12,s8,x7/1,pn/d,s8,x4/14,s2,x7/6,s10,x11/8,s9,x4/12,s7,x1/9,po/m,x11/13,s9,pc/d,x0/1,s4,x8/11,pi/e,x2/0,pg/a,x9/5,s7,x0/3,s9,x5/9,s5,x15/14,pb/c,x8/12,s11,x10/6,pl/h,x5/3,s9,x15/0,s5,x3/5,s9,x0/12,s9,x2/6,s5,x8/10,pj/c,s13,x12/11,pf/a,s7,pn/m,x9/1,s15,x4/6,pe/j,x15/3,s6,x0/12,s7,x2/7,pn/c,x9/11,s9,x15/1,pp/l,x0/14,s14,x5/8,s10,x3/14,s13,x9/7,s7,x6/11,s14,x8/12,pn/m,x7/4,ph/o,x14/11,s4,pc/k,x4/12,s7,x5/15,pd/e,x2/9,s11,x14/4,s2,x7/12,pm/f,x11/4,s1,x10/5,s11,x4/15,pp/l,x8/13,pj/n,x9/15,po/k,s2,x12/14,pm/a,x9/10,s3,x13/5,s13,x0/9,s3,x5/8,s13,pg/k,x13/2,s11,x0/6,s7,x9/14,s8,pj/i,x3/1,s15,x2/11,po/c,x7/5,pg/l,x13/9,pn/m,x2/7,s5,x11/1,s13,x8/2,pd/l,x14/13,s9,x2/4,s10,x12/6,pm/b,x14/13'.split(',')
        self.assertEqual(target.calc(dance, 16, 5001), 'midgneohckafjlpb')

if __name__ == '__main__':
    unittest.main()
