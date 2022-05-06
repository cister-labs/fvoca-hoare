import unittest
from Specs import *

''' In this test file, we are mostly concerned
    with testing that the conditions imposed upon
    instantiation of [AExpr], [BExpr], and [Spec] is
    properly implemented.
    
    For that, we create the expressions and check if
    they are from the right class instances. In case
    wrong arguments to build expressions and assertions
    are provided, the test is expected to fail.
    '''

class TestSpecs(unittest.TestCase):

    # 1.
    def test_p1(self):
        self.assertIsInstance(SEq(AEVar('i'),AEVal(5)),SEq)
        self.assertIsInstance(SAnd(SEq(AEVar('a'),AEVal(7)),SEq(AEVar('i'),AEVal(5))),SAnd)

    # 2.
    def test_p2(self):
        self.assertIsInstance(SEq(AEVar('i'),AEVal(5)),SEq)
        self.assertIsInstance(SAnd(SEq(AEVar('a'),AEVal(7)),SGt(AEVar('i'),AEVal(0))),SAnd)

    # 3.
    def test_p3(self):
        self.assertIsInstance(SAnd(SEq(AEVar('i'),AEVal(5)),SEq(AEVar('a'),AEVal(3))),SAnd)
        self.assertIsInstance(SEq(AEVar('a'),AEVal(7)),SEq)

    # 4.
    def test_p4(self):
        self.assertIsInstance(SEq(AEVar('a'),AEVal(7)),SEq)
        self.assertIsInstance(SEq(AEVar('a'),AEVal(7)),SEq)

    # 5.
    def test_p5(self):
        self.assertIsInstance(SEq(AEVar('i'),AEMinus(AEVar('a'),AEVal(1))),SEq)
        self.assertIsInstance(SEq(AEVar('i'),AEPlus(AEVar('a'),AEVal(1))),SEq)

    # 6.
    def test_p6(self):
        self.assertIsInstance(SVal(True),SVal)
        self.assertIsInstance(SEq(AEVar('i'),AEPlus(AEVar('a'),AEVal(2))),SEq)

    # 7.
    def test_p7(self):
        self.assertIsInstance(SGt(AEVar('a'),AEVar('b')),SGt)
        self.assertIsInstance(SGt(AEMult(AEVar('m'),AEVar('n')),AEVal(0)),SGt)

    # 8.
    def test_p8(self):
        self.assertIsInstance(SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i'))),SEq)
        self.assertIsInstance(SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i'))),SEq)

    # 9.
    def test_p9(self):
        self.assertIsInstance(SVal(True),SVal)
        self.assertIsInstance(SAnd(SLeq(AEVar('min'),AEVar('i')),SLeq(AEVar('min'),AEVar('i'))),SAnd)

    # 10.
    def test_p10(self):
        self.assertIsInstance(SAnd(SGt(AEVar('i'),AEVal(0)),SGt(AEVar('j'),AEVal(0))),SAnd)
        self.assertIsInstance(SGt(AEVar('min'),AEVal(0)),SGt)

    # 11.
    def test_p11(self):
        self.assertIsInstance(SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i'))),SEq)
        self.assertIsInstance(SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i'))),SEq)        

if __name__ == '__main__':
    unittest.main()