import unittest

from VCs import *

''' File that tests the correction of the algorithms for
    the generation of verification conditions. In each
    test, the [VC] is tested, followed by [VCG]. These
    functions correspond to those introduced in the 
    theoretical classes. '''


class Test_VCs(unittest.TestCase):

    # 1.
    def test_vcs_1(self):
        p1_pre  = SEq(AEVar('i'),AEVal(5))
        p1_comm = Assgn('a',AEPlus(AEVar('i'),AEVal(2)))
        p1_post = SAnd(SEq(AEVar('a'),AEVal(7)),SEq(AEVar('i'),AEVal(5)))
        p1_vc1  = { SImp(
                        SEq(AEVar('i'),AEVal(5)),
                        SAnd(SEq(AEPlus(AEVar('i'),AEVal(2)),AEVal(7)),
                             SEq(AEVar('i'),AEVal(5))))
                    }
        self.assertEqual(VC(p1_pre,p1_comm,p1_post),p1_vc1) 
        self.assertEqual(VCG(p1_pre,p1_comm,p1_post),p1_vc1) 


    # 2.
    def test_vcs_2(self):
        p2_pre  = SEq(AEVar('i'),AEVal(5))
        p2_comm = Assgn('a',AEPlus(AEVar('i'),AEVal(2)))
        p2_post = SAnd(SEq(AEVar('a'),AEVal(7)),SGt(AEVar('i'),AEVal(0)))
        p2_vc1  = { SImp(
                        SEq(AEVar('i'),AEVal(5)),
                        SAnd(SEq(AEPlus(AEVar('i'),AEVal(2)),AEVal(7)),
                             SGt(AEVar('i'),AEVal(0))))
                    }
        self.assertEqual(VC(p2_pre,p2_comm,p2_post),p2_vc1) 
        self.assertEqual(VCG(p2_pre,p2_comm,p2_post),p2_vc1)

    # 3.
    def test_vcs_3(self):
        p3_pre  = SAnd(SEq(AEVar('i'),AEVal(5)),SEq(AEVar('a'),AEVal(3)))
        p3_comm = Assgn('a',AEPlus(AEVar('i'),AEVal(2)))
        p3_post = SEq(AEVar('a'),AEVal(7))
        p3_vc1  = { SImp(
                        SAnd(SEq(AEVar('i'),AEVal(5)),SEq(AEVar('a'),AEVal(3))),
                             SEq(AEPlus(AEVar('i'),AEVal(2)),AEVal(7))
                    )}
        self.assertEqual(VC(p3_pre,p3_comm,p3_post),p3_vc1) 
        self.assertEqual(VCG(p3_pre,p3_comm,p3_post),p3_vc1)

    # 4.
    def test_vcs_4(self):
        p4_pre  = SEq(AEVar('a'),AEVal(7))
        p4_comm = Assgn('i',AEPlus(AEVar('i'),AEVal(2)))
        p4_post = SEq(AEVar('a'),AEVal(7))
        p4_vc1  = { SImp(SEq(AEVar('a'),AEVal(7)),SEq(AEVar('a'),AEVal(7))) }
        self.assertEqual(VC(p4_pre,p4_comm,p4_post),p4_vc1) 
        self.assertEqual(VCG(p4_pre,p4_comm,p4_post),p4_vc1)

    # 5.
    def test_vcs_5(self):
        p5_pre  = SEq(AEVar('i'),AEMinus(AEVar('a'),AEVal(1)))
        p5_comm = Assgn('i',AEPlus(AEVar('i'),AEVal(2)))
        p5_post = SEq(AEVar('i'),AEPlus(AEVar('a'),AEVal(1)))
        p5_vc1  = { SImp(
                        SEq(AEVar('i'),AEMinus(AEVar('a'),AEVal(1))),
                        SEq(AEPlus(AEVar('i'),AEVal(2)),AEPlus(AEVar('a'),AEVal(1)))) 
                }
        self.assertEqual(VC(p5_pre,p5_comm,p5_post),p5_vc1) 
        self.assertEqual(VCG(p5_pre,p5_comm,p5_post),p5_vc1)

    # 6.
    def test_vcs_6(self):
        p6_pre  = SVal(True)
        p6_comm = Assgn('a',AEPlus(AEVar('i'),AEVal(2)))
        p6_post = SEq(AEVar('a'),AEPlus(AEVar('i'),AEVal(2)))
        p6_vc1  = { SImp(
                        SVal(True),
                        SEq(AEPlus(AEVar('i'),AEVal(2)),AEPlus(AEVar('i'),AEVal(2)))
                    )
        }
        self.assertEqual(VC(p6_pre,p6_comm,p6_post),p6_vc1) 
        self.assertEqual(VCG(p6_pre,p6_comm,p6_post),p6_vc1)

    # 7.
    def test_vcs_7(self):
        p7_pre  = SGt(AEVar('a'),AEVar('b'))
        p7_comm = Seq(Assgn('m',AEVal(1)),Assgn('n',AEMinus(AEVar('a'),AEVar('b'))))
        p7_post = SGt(AEMult(AEVar('m'),AEVar('n')),AEVal(0))
        p7_vc1  = {
            SImp(SGt(AEMult(AEVar('m'),AEMinus(AEVar('a'),AEVar('b'))),AEVal(0)),
                 SGt(AEMult(AEVar('m'),AEMinus(AEVar('a'),AEVar('b'))),AEVal(0))),
            SImp(SGt(AEVar('a'),AEVar('b')),
                 SGt(AEMult(AEVal(1),AEMinus(AEVar('a'),AEVar('b'))),AEVal(0)))
        }
        p7_vc2  = { SImp(SGt(AEVar('a'),AEVar('b')),
                    SGt(AEMult(AEVal(1),AEMinus(AEVar('a'),AEVar('b'))),AEVal(0)))}
        self.assertEqual(VC(p7_pre,p7_comm,p7_post),p7_vc1)
        self.assertEqual(VCG(p7_pre,p7_comm,p7_post),p7_vc2)

    # 8.
    def test_vcs_8(self):
        p8_pre  = SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i')))
        p8_comm = Seq(Assgn('i',AEPlus(AEVar('i'),AEVal(1))),Assgn('s',AEMult(AEVar('s'),AEVal(2))))
        p8_post = SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i')))
        p8_vc1  = {
            SImp(SEq(AEMult(AEVar('s'),AEVal(2)),AEPow(AEVal(2),AEVar('i'))),
                 SEq(AEMult(AEVar('s'),AEVal(2)),AEPow(AEVal(2),AEVar('i')))),
            SImp(SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i'))),
                 SEq(AEMult(AEVar('s'),AEVal(2)),AEPow(AEVal(2),AEPlus(AEVar('i'),AEVal(1)))))
        }
        p8_vc2 = {
            SImp(SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i'))),
                 SEq(AEMult(AEVar('s'),AEVal(2)),AEPow(AEVal(2),AEPlus(AEVar('i'),AEVal(1)))))
        }
        self.assertEqual(VC(p8_pre,p8_comm,p8_post),p8_vc1)
        self.assertEqual(VCG(p8_pre,p8_comm,p8_post),p8_vc2)

    # 9.
    def test_vcs_9(self):
        p9_pre = SVal(True)
        p9_comm = IfThen(BELt(AEVar('i'),AEVar('j')),Assgn('min',AEVar('i')),Assgn('min',AEVar('j')))
        p9_post = SAnd(SLeq(AEVar('min'),AEVar('i')),SLeq(AEVar('min'),AEVar('i')))
        p9_vc1 = {
            SImp(
                SAnd(SVal(True),SNeg(SLt(AEVar('i'),AEVar('j')))),
                SAnd(SLeq(AEVar('j'),AEVar('i')),SLeq(AEVar('j'),AEVar('i')))),
            SImp(
                SAnd(SVal(True),SLt(AEVar('i'),AEVar('j'))),
                SAnd(SLeq(AEVar('i'),AEVar('i')),SLeq(AEVar('i'),AEVar('i'))))
        }
        p9_vc2 = {
            SImp(SVal(True),
                 SAnd(SImp(SLt(AEVar('i'),AEVar('j')),
                        SAnd(SLeq(AEVar('i'),AEVar('i')),SLeq(AEVar('i'),AEVar('i')))),
                      SImp(SNeg(SLt(AEVar('i'),AEVar('j'))),
                        SAnd(SLeq(AEVar('j'),AEVar('i')),SLeq(AEVar('j'),AEVar('i'))))))
        }
        self.assertEqual(VC(p9_pre,p9_comm,p9_post),p9_vc1)
        self.assertEqual(VCG(p9_pre,p9_comm,p9_post),p9_vc2)

    # 10.
    def test_vcs_10(self):
        p10_pre = SAnd(SGt(AEVar('i'),AEVal(0)),SGt(AEVar('j'),AEVal(0)))
        p10_comm = IfThen(BELt(AEVar('i'),AEVar('j')),Assgn('min',AEVar('i')),Assgn('min',AEVar('j')))
        p10_post = SGt(AEVar('min'),AEVal(0))
        p10_vc1  = {
            SImp(
                SAnd(SAnd(SGt(AEVar('i'),AEVal(0)),SGt(AEVar('j'),AEVal(0))),
                          SNeg(SLt(AEVar('i'),AEVar('j')))),
                SGt(AEVar('j'),AEVal(0))),
            SImp(
                SAnd(SAnd(SGt(AEVar('i'),AEVal(0)),SGt(AEVar('j'),AEVal(0))),
                          SLt(AEVar('i'),AEVar('j'))),           
                SGt(AEVar('i'),AEVal(0)))
        }
        p10_vc2  = {
            SImp(
                SAnd(SGt(AEVar('i'),AEVal(0)),SGt(AEVar('j'),AEVal(0))),
                SAnd(
                    SImp(SLt(AEVar('i'),AEVar('j')),SGt(AEVar('i'),AEVal(0))),
                    SImp(SNeg(SLt(AEVar('i'),AEVar('j'))),SGt(AEVar('j'),AEVal(0)))
                ))
        }
        self.assertEqual(VC(p10_pre,p10_comm,p10_post),p10_vc1)
        self.assertEqual(VCG(p10_pre,p10_comm,p10_post),p10_vc2)

    # 11.
    def test_vcs_11(self):
        p11_pre = SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i')))
        p11_comm = While(BELt(AEVar('i'),AEVar('n')),
                    SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i'))),
                    Seq(Assgn('i',AEPlus(AEVar('i'),AEVal(1))),
                        Assgn('s',AEMult(AEVar('s'),AEVal(2)))))
        p11_post = SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i')))
        p11_vc_aux1 = SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i')))
        p11_vc1  = {
            SImp(SAnd(SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i'))),SNeg(SLt(AEVar('i'),AEVar('n')))), 
                 SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i')))),
            SImp(SEq(AEMult(AEVar('s'),AEVal(2)),AEPow(AEVal(2),AEVar('i'))),
                 SEq(AEMult(AEVar('s'),AEVal(2)),AEPow(AEVal(2),AEVar('i')))),
            SImp(SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i'))),
                 SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i')))),
            SImp(SAnd(SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i'))),SNeg(SLt(AEVar('i'),AEVar('n')))), 
                 SEq(AEMult(AEVar('s'),AEVal(2)),AEPow(AEVal(2),AEPlus(AEVar('i'),AEVal(1)))))     
        }
        p11_vc2  = {
            SImp(SAnd(SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i'))),SNeg(SLt(AEVar('i'),AEVar('n')))), 
                 SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i')))),
            SImp(SAnd(SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i'))),SLt(AEVar('i'),AEVar('n'))), 
                 SEq(AEMult(AEVar('s'),AEVal(2)),AEPow(AEVal(2),AEPlus(AEVar('i'),AEVal(1))))),
            SImp(SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i'))),
                 SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i'))))
        }
        self.assertEqual(VC(p11_pre,p11_comm,p11_post),p11_vc1)
        self.assertEqual(VCG(p11_pre,p11_comm,p11_post),p11_vc2)

if __name__ == '__main__':
    unittest.main()