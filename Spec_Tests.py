from colorama import init, Fore, Back, Style

from Exprs import *
from Imp   import *
from Specs import *

init(autoreset=True)

ae1 = AEMinus(AEVar('x'),AEVar('z'))
print(ae1)
ae2 = AEPlus(AEVar('y'),AEVal(1))
print(ae2)
r = spec_subst(ae1,'z',ae2)
print(r)

cmd = Assgn('x',spec_subst(ae1,'z',ae2))
print(cmd)

z = SForall('x',SImp(BEEq(AEVar('x'),AEVar('x')),BEAnd(BEVal(True),BEVal(False))))
print(z)

p = While(
        BEEq(AEVar('x'),AEVal(0)),
        SAtom(BEEq(AEVar('x'),AEVal(0))),
        Assgn('x',AEMinus(AEVar('x'),AEVal(1)))
    )
print(p)