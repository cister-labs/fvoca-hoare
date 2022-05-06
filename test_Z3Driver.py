import unittest
from Z3Driver import *

class Test_Z3Driver(unittest.TestCase):

    # 1.
    def test_z3_1(self):
        p1_pre  = SEq(AEVar('i'),AEVal(5))
        p1_comm = Assgn('a',AEPlus(AEVar('i'),AEVal(2)))
        p1_post = SAnd(SEq(AEVar('a'),AEVal(7)),SEq(AEVar('i'),AEVal(5)))
        self.assertEqual(prove_correct_VC(p1_pre,p1_comm,p1_post),unsat)

    # 2.
    def test_z3_2(self):
        p2_pre  = SEq(AEVar('i'),AEVal(5))
        p2_comm = Assgn('a',AEPlus(AEVar('i'),AEVal(2)))
        p2_post = SAnd(SEq(AEVar('a'),AEVal(7)),SGt(AEVar('i'),AEVal(0)))
        self.assertEqual(prove_correct_VC(p2_pre,p2_comm,p2_post),unsat)

    # 3.
    def test_z3_3(self):
        p3_pre  = SAnd(SEq(AEVar('i'),AEVal(5)),SEq(AEVar('a'),AEVal(3)))
        p3_comm = Assgn('a',AEPlus(AEVar('i'),AEVal(2)))
        p3_post = SEq(AEVar('a'),AEVal(7))
        self.assertEqual(prove_correct_VC(p3_pre,p3_comm,p3_post),unsat)

    # 4.
    def test_z3_4(self):
        p4_pre  = SEq(AEVar('a'),AEVal(7))
        p4_comm = Assgn('i',AEPlus(AEVar('i'),AEVal(2)))
        p4_post = SEq(AEVar('a'),AEVal(7))
        self.assertEqual(prove_correct_VC(p4_pre,p4_comm,p4_post),unsat)

    # 5.
    def test_z3_5(self):
        p5_pre  = SEq(AEVar('i'),AEMinus(AEVar('a'),AEVal(1)))
        p5_comm = Assgn('i',AEPlus(AEVar('i'),AEVal(2)))
        p5_post = SEq(AEVar('i'),AEPlus(AEVar('a'),AEVal(1)))
        self.assertEqual(prove_correct_VC(p5_pre,p5_comm,p5_post),unsat)

    # 6.
    def test_z3_6(self):
        p6_pre  = SVal(True)
        p6_comm = Assgn('i',AEPlus(AEVar('i'),AEVal(2)))
        p6_post = SEq(AEVar('i'),AEPlus(AEVar('a'),AEVal(2)))
        self.assertEqual(prove_correct_VC(p6_pre,p6_comm,p6_post),unsat)

    # 7.
    def test_z3_7(self):
        p7_pre  = SGt(AEVar('a'),AEVar('b'))
        p7_comm = Seq(Assgn('m',AEVal(1)),Assgn('n',AEMinus(AEVar('a'),AEVar('b'))))
        p7_post = SGt(AEMult(AEVar('m'),AEVar('n')),AEVal(0))
        self.assertEqual(prove_correct_VC(p7_pre,p7_comm,p7_post),unsat)

    # 8.
    def test_z3_8(self):
        p8_pre  = SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i')))
        p8_comm = Seq(Assgn('i',AEPlus(AEVar('i'),AEVal(1))),Assgn('s',AEMult(AEVar('s'),AEVal(2))))
        p8_post = SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i')))
        self.assertEqual(prove_correct_VC(p8_pre,p8_comm,p8_post),unsat)

    # 9.
    def test_z3_9(self):
        p9_pre = SVal(True)
        p9_comm = IfThen(BELt(AEVar('i'),AEVar('j')),Assgn('min',AEVar('i')),Assgn('min',AEVar('j')))
        p9_post = SAnd(SLeq(AEVar('min'),AEVar('i')),SLeq(AEVar('min'),AEVar('i')))
        self.assertEqual(prove_correct_VC(p9_pre,p9_comm,p9_post),unsat)

    # 10.
    def test_z3_10(self):
        p10_pre = SAnd(SGt(AEVar('i'),AEVal(0)),SGt(AEVar('j'),AEVal(0)))
        p10_comm = IfThen(BELt(AEVar('i'),AEVar('j')),Assgn('min',AEVar('i')),Assgn('min',AEVar('j')))
        p10_post = SGt(AEVar('min'),AEVal(0))
        self.assertEqual(prove_correct_VC(p10_pre,p10_comm,p10_post),unsat)

    # 11.
    def test_z3_11(self):
        p11_pre = SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i')))
        p11_comm = While(BELt(AEVar('i'),AEVar('n')),
                    SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i'))),
                    Seq(Assgn('i',AEPlus(AEVar('i'),AEVal(1))),
                        Assgn('s',AEMult(AEVar('s'),AEVal(2)))))
        p11_post = SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i')))
        self.assertEqual(prove_correct_VC(p11_pre,p11_comm,p11_post),unsat)

if __name__ == '__main__':
    unittest.main()