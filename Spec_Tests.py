from typing import Iterator
from colorama import init, Fore, Back, Style

from Exprs import *
from Imp   import *
from Specs import *
from WPrec import *
from VCs   import *
from Z3Driver import *

init(autoreset=True)

sp = SAnd(
    SEq(AEVar('r'),AEPow(AEVar('n'),AEVar('i'))),
    SAnd(
        SLeq(AEVal(0),AEVar('i')),
        SAnd(
            SLeq(AEVar('i'),AEVar('m')),
            SGt(AEVar('n'),AEVal(0))
        )
    )
)

print(sp)


p = Seq(
        Assgn('r',AEVal(1)),
        Seq(
            Assgn('i',AEVal(0)),
            While(
                BELt(AEVar('i'),AEVar('m')),
                sp,
                Seq(
                    Assgn('r',AEMult(AEVar('r'),AEVar('n'))),
                    Assgn('i',AEMinus(AEVar('i'),AEVal(1)))
                )
            )
        )
)

post = SEq(
        AEVar('r'),
        AEPow(AEVar('n'),AEVar('m'))
)

pre = SAnd(
        SGt(AEVar('n'),AEVal(0)),
        SGeq(AEVar('m'),AEVal(0))
)


print(p)
print("\n\n\n")
print(wprec(p,post))
print("\n\n\n")
vcs = VC(pre,p,post)
s = set([])
for x in vcs:
#    print(f'Assertion : {x}')
    s = s.union(spec_vars(x))
#    print(s)

vars = dict()
for i in s:
    vars[i] = Int(i)
    print(i)

for a in vcs:
    print(f'Assertion: {a}')
    print(f'Z3: {spec2z3(a,vars)}')

t = prove_vcs(vcs,vars)
print(t)

# e = AEPlus(AEVar('x'),AEPow(AEVal(2),AEVal(3)))
# k = ae2z3(e,{'x':Int('x')})
# print(k)

# l = spec2z3(pre,{'n':Int('n') , 'm':Int('m')})
# print(l)