#from lib2to3.pgen2.literals import evalString
from z3 import *
from Specs import *

def spec_vars_ae(e):
    if isinstance(e,AEVar):
        return set([e.name()])
    elif isinstance(e,AEVal):
        return set()
    elif isinstance(e,AEPow):
        e1 = spec_vars_ae(e.base())
        e2 = spec_vars_ae(e.exp())
        return e1.union(e2)
    elif isinstance(e,(AEPlus,AEMinus,AEMult)):
        e1 = spec_vars_ae(e.inner_l())
        e2 = spec_vars_ae(e.inner_r())
        return e1.union(e2)

def spec_vars(e):
    if isinstance(e,SVal):
        return set()
    elif isinstance(e,SNeg):
        return spec_vars(e.value())
    elif isinstance(e,(SAnd,SOr,SImp)):
        e1 = spec_vars(e.left())
        e2 = spec_vars(e.right())
        return e1.union(e2)
    elif isinstance(e,(SLeq,SLt,SEq,SGeq,SGt)):
        e1 = spec_vars_ae(e.left())
        e2 = spec_vars_ae(e.right())
        return e1.union(e2)

def ae2z3(e,vars):
    if isinstance(e,AEVal):
        return IntVal(e.value())
    elif isinstance(e,AEVar):
        return vars[e.name()]
    elif isinstance(e,AEPow):
        l = ae2z3(e.base(),vars)
        r = ae2z3(e.exp(),vars)
        return (l**r)
    elif isinstance(e,AEPlus):
        l = ae2z3(e.inner_l(),vars)
        r = ae2z3(e.inner_r(),vars)
        return (l + r)
    elif isinstance(e,AEMinus):
        l = ae2z3(e.inner_l(),vars)
        r = ae2z3(e.inner_r(),vars)
        return (l - r)
    elif isinstance(e,AEMult):
        l = ae2z3(e.inner_l(),vars)
        r = ae2z3(e.inner_r(),vars)
        return (l * r)

def spec2z3(e,vars):
    if isinstance(e,SVal):
        return BoolVal(e.value())
    elif isinstance(e,SNeg):
        l = spec2z3(e.value(),vars)
        return Not(l)
    elif isinstance(e,SAnd):
        l = spec2z3(e.left(),vars)
        r = spec2z3(e.right(),vars)
        return And([l,r])
    elif isinstance(e,SOr):
        l = spec2z3(e.left(),vars)
        r = spec2z3(e.right(),vars)
        return Or([l,r])
    elif isinstance(e,SImp):
        l = spec2z3(e.left(),vars)
        r = spec2z3(e.right(),vars)
        return Implies(l,r)
    elif isinstance(e,SEq):
        l = ae2z3(e.left(),vars)
        r = ae2z3(e.right(),vars)
        return (l == r)
    elif isinstance(e,SLt):
        l = ae2z3(e.left(),vars)
        r = ae2z3(e.right(),vars)
        return (l < r)
    elif isinstance(e,SLeq):
        l = ae2z3(e.left(),vars)
        r = ae2z3(e.right(),vars)
        return (l <= r)
    elif isinstance(e,SGt):
        l = ae2z3(e.left(),vars)
        r = ae2z3(e.right(),vars)
        return (l > r)
    elif isinstance(e,SGeq):
        l = ae2z3(e.left(),vars)
        r = ae2z3(e.right(),vars)
        return (l >= r)

def prove_vcs(vcs,vars):
    s = Solver()
    for vc in vcs:
        # We negate each of the formulae so that if Z3 says unsat
        # then we know it is a theorem.
        s.add(Not(spec2z3(vc,vars)))
    print(s)
    return s.check()

#def vc2z3(s):
