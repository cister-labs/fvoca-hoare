from typing import Iterator
from colorama import init, Fore, Back, Style

from Exprs import *
from Imp   import *
from Specs import *
from WPrec import *
from VCs   import *
from Z3Driver import *

init(autoreset=True)

''' Examples extracted from exercise sheet on Hoare Logic.
    See: 
'''

# 1.
p1_pre  = SEq(AEVar('i'),AEVal(5))
p1_comm = Assgn('a',AEPlus(AEVar('i'),AEVal(2)))
p1_post = SAnd(SEq(AEVar('a'),AEVal(7)),SEq(AEVar('i'),AEVal(5)))

# 2.
p2_pre  = SEq(AEVar('i'),AEVal(5))
p2_comm = Assgn('a',AEPlus(AEVar('i'),AEVal(2)))
p2_post = SAnd(SEq(AEVar('a'),AEVal(7)),SGt(AEVar('i'),AEVal(0)))

# 3.
p3_pre  = SAnd(SEq(AEVar('i'),AEVal(5)),SEq(AEVar('a'),AEVal(3)))
p3_comm = Assgn('a',AEPlus(AEVar('i'),AEVal(2)))
p3_post = SEq(AEVar('a'),AEVal(7))

# 4.
p4_pre  = SEq(AEVar('a'),AEVal(7))
p4_comm = Assgn('i',AEPlus(AEVar('i'),AEVal(2)))
p4_post = SEq(AEVar('a'),AEVal(7))

# 5.
p5_pre  = SEq(AEVar('i'),AEMinus(AEVar('a'),AEVal(1)))
p5_comm = Assgn('i',AEPlus(AEVar('i'),AEVal(2)))
p5_post = SEq(AEVar('i'),AEPlus(AEVar('a'),AEVal(1)))

# 6.
p6_pre  = SVal(True)
p6_comm = Assgn('i',AEPlus(AEVar('i'),AEVal(2)))
p6_post = SEq(AEVar('i'),AEPlus(AEVar('a'),AEVal(2)))

# 7.
p7_pre  = SGt(AEVar('a'),AEVar('b'))
p7_comm = Seq(Assgn('m',AEVal(1)),Assgn('n',AEMinus(AEVar('a'),AEVar('b'))))
p7_post = SGt(AEMult(AEVar('m'),AEVar('n')),AEVal(0))

# 8.
p8_pre  = SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i')))
p8_comm = Seq(Assgn('i',AEPlus(AEVar('i'),AEVal(1))),Assgn('s',AEMult(AEVar('s'),AEVal(2))))
p8_post = SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i')))

# 9.
p9_pre = SVal(True)
p9_comm = IfThen(BELt(AEVar('i'),AEVar('j')),Assgn('min',AEVar('i')),Assgn('min',AEVar('j')))
p9_post = SAnd(SLeq(AEVar('min'),AEVar('i')),SLeq(AEVar('min'),AEVar('i')))

# 10.
p10_pre = SAnd(SGt(AEVar('i'),AEVal(0)),SGt(AEVar('j'),AEVal(0)))
p10_comm = IfThen(BELt(AEVar('i'),AEVar('j')),Assgn('min',AEVar('i')),Assgn('min',AEVar('j')))
p10_post = SGt(AEVar('min'),AEVal(0))

# 11.
p11_pre = SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i')))
p11_comm = While(BELt(AEVar('i'),AEVar('n')),
            SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i'))),
            Seq(Assgn('i',AEPlus(AEVar('i'),AEVal(1))),
                Assgn('s',AEMult(AEVar('s'),AEVal(2)))))
p11_post = SEq(AEVar('s'),AEPow(AEVal(2),AEVar('i')))

for i in range(1,12):
    pre  = globals()['p'+str(i)+'_pre']
    c    = globals()['p'+str(i)+'_comm']
    post = globals()['p'+str(i)+'_post']
    r = prove_correct(pre,c,post)
    print(f'Ex {i}) Checking Results ==> {r}!')

#k = wprec(p1_comm,p1_post)
#print(k)







# #print(p)
# #print("\n\n\n")
# #print(wprec(p,post))
# #print("\n\n\n")
# print("Call VCG:")
# vcs = VCG(pre,p,post)
# # s = set([])
# for x in vcs:
#     print(f'Assertion : {x}')
# #     s = s.union(spec_vars(x))
# #    print(s)

# # vars = dict()
# # for i in s:
# #     vars[i] = Int(i)
# #     print(i)

# # for a in vcs:
# #     print(f'Assertion: {a}')
# #     print(f'Z3: {spec2z3(a,vars)}')

# # t = prove_vcs(vcs,vars)
# # print(t)

# # # e = AEPlus(AEVar('x'),AEPow(AEVal(2),AEVal(3)))
# # # k = ae2z3(e,{'x':Int('x')})
# # # print(k)

# # # l = spec2z3(pre,{'n':Int('n') , 'm':Int('m')})
# # # print(l)