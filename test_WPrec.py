import unittest
from WPrec import *

''' File that tests the correction of the weakest precondition
    generation function as introduced in the theoretical
    classes. '''


class TestWPrec(unittest.TestCase):

    # 1.
    def test_wprec_1(self):
        p1_comm = Assgn('a',AEPlus(AEVar('i'),AEVal(2)))
        p1_post = SAnd(SEq(AEVar('a'),AEVal(7)),SEq(AEVar('i'),AEVal(5)))
        p1_answ = SAnd(SEq(AEPlus(AEVar('i'),AEVal(2)),AEVal(7)),SEq(AEVar('i'),AEVal(5)))
        self.assertEqual(wprec(p1_comm,p1_post),p1_answ)

    # 2.
    def test_wprec_2(self):
        p2_comm = Assgn('a',AEPlus(AEVar('i'),AEVal(2)))
        p2_post = SAnd(SEq(AEVar('a'),AEVal(7)),SGt(AEVar('i'),AEVal(0)))
        p2_answ = SAnd(SEq(AEPlus(AEVar('i'),AEVal(2)),AEVal(7)),SGt(AEVar('i'),AEVal(0)))
        self.assertEqual(wprec(p2_comm,p2_post),p2_answ)

    # 3.
    def test_wprec_3(self):
        p3_comm = Assgn('a',AEPlus(AEVar('i'),AEVal(2)))
        p3_post = SEq(AEVar('a'),AEVal(7))
        p3_answ = SEq(AEPlus(AEVar('i'),AEVal(2)),AEVal(7))
        self.assertEqual(wprec(p3_comm,p3_post),p3_answ)

    # 4.
    def test_wprec_4(self):
        p4_comm = Assgn('i',AEPlus(AEVar('i'),AEVal(2)))
        p4_post = SEq(AEVar('a'),AEVal(7))
        p4_answ = SEq(AEVar('a'),AEVal(7))
        self.assertEqual(wprec(p4_comm,p4_post),p4_answ)

    # 5.
    def test_wprec_5(self):
        p5_comm = Assgn('i',AEPlus(AEVar('i'),AEVal(2)))
        p5_post = SEq(AEVar('i'),AEPlus(AEVar('a'),AEVal(1)))
        p5_answ = SEq(AEPlus(AEVar('i'),AEVal(2)),AEPlus(AEVar('a'),AEVal(1)))
        self.assertEqual(wprec(p5_comm,p5_post),p5_answ)

    # 6.
    def test_wprec_6(self):
        p6_comm = Assgn('a',AEPlus(AEVar('i'),AEVal(2)))
        p6_post = SEq(AEVar('a'),AEPlus(AEVar('i'),AEVal(2)))
        p6_answ = SEq(AEPlus(AEVar('i'),AEVal(2)),AEPlus(AEVar('i'),AEVal(2)))
        self.assertEqual(wprec(p6_comm,p6_post),p6_answ)

    # 7.
    def test_wprec_7(self):
        p7_comm = Seq(Assgn('m',AEVal(1)),Assgn('n',AEMinus(AEVar('a'),AEVar('b'))))
        p7_post = SGt(AEMult(AEVar('m'),AEVar('n')),AEVal(0))
        p7_answ = SGt(AEMult(AEVal(1),AEMinus(AEVar('a'),AEVar('b'))),AEVal(0))
        self.assertEqual(wprec(p7_comm,p7_post),p7_answ)

    # 8.
    def test_wprec_8(self):
        p8_comm = Seq(Assgn('i',AEPlus(AEVar('i'),AEVal(1))),Assgn('s',AEMult(AEVar('s'),AEVal(2))))
        p8_post = SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i')))
        p8_answ = SEq(AEMult(AEVar('s'),AEVal(2)),AEPow(AEVal(2),AEPlus(AEVar('i'),AEVal(1))))
        self.assertEqual(wprec(p8_comm,p8_post),p8_answ)

    # 9.
    def test_wprec_(self):
        p9_comm = IfThen(BELt(AEVar('i'),AEVar('j')),Assgn('min',AEVar('i')),Assgn('min',AEVar('j')))
        p9_post = SAnd(SLeq(AEVar('min'),AEVar('i')),SLeq(AEVar('min'),AEVar('i')))
        p9_answl = SImp(
                    SLt(AEVar('i'),AEVar('j')),
                        SAnd(SLeq(AEVar('i'),AEVar('i')),SLeq(AEVar('i'),AEVar('i'))))
        p9_answr = SImp(
                    SNeg(SLt(AEVar('i'),AEVar('j'))),
                    SAnd(SLeq(AEVar('j'),AEVar('i')),SLeq(AEVar('j'),AEVar('i'))))

        p9_answ = SAnd(p9_answl,p9_answr) 
        self.assertEqual(wprec(p9_comm,p9_post),p9_answ)
        

    # 10.
    def test_wprec_10(self):
        p10_comm = IfThen(BELt(AEVar('i'),AEVar('j')),Assgn('min',AEVar('i')),Assgn('min',AEVar('j')))
        p10_post = SGt(AEVar('min'),AEVal(0))
        p10_answ = SAnd(
            SImp(SLt(AEVar('i'),AEVar('j')),SGt(AEVar('i'),AEVal(0))),
            SImp(SNeg(SLt(AEVar('i'),AEVar('j'))),SGt(AEVar('j'),AEVal(0)))
        )
        self.assertEqual(wprec(p10_comm,p10_post),p10_answ)

    # 11.
    def test_wprec_11(self):
        p11_comm = While(BELt(AEVar('i'),AEVar('n')),
            SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i'))),
            Seq(Assgn('i',AEPlus(AEVar('i'),AEVal(1))),
                Assgn('s',AEMult('s',AEVal(2)))))
        p11_post = SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i')))
        p11_anwr = SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i')))
        self.assertEqual(wprec(p11_comm,p11_post),p11_anwr)

if __name__ == '__main__':
    unittest.main()