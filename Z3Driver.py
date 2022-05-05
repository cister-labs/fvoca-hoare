from z3 import *
from Specs import *

''' The function [spec_vars_ae] identifies all free
    variables in an arithmetic expression and gathers
    them in a set. '''

def spec_vars_ae(e):
    match e:
        case AEVar():
            return set([e.name()])
        case AEVal():
            return set()
        case AEPow():
            e1 = spec_vars_ae(e.base())
            e2 = spec_vars_ae(e.exp())
            return e1.union(e2)
        case AEPlus() | AEMinus() | AEMult():
            e1 = spec_vars_ae(e.left())
            e2 = spec_vars_ae(e.right())
            return e1.union(e2)

''' The function [spec_vars] identifies all free
    variables in a specification and gathers
    them in a set. '''

def spec_vars(e):

    match e:
        case SVal():
            return set()
        case SNeg():
            return spec_vars(e.value())
        case SAnd() | SOr() | SImp():
            e1 = spec_vars(e.left())
            e2 = spec_vars(e.right())
            return e1.union(e2)
        case SLeq() | SLt() | SEq() | SGeq() | SGt():
            e1 = spec_vars_ae(e.left())
            e2 = spec_vars_ae(e.right())
            return e1.union(e2)

''' The function [ae2z3] transforms an arithmetic expression
    built using the [AExpr] class hierarchy into the 
    corresponding format accepted by the Z3 theorem
    prover. '''

def ae2z3(e,vars):

    match e:
        case AEVal():
            return IntVal(e.value())
        case AEVar():
            return vars[e.name()]
        case AEPow():
            l = ae2z3(e.base(),vars)
            r = ae2z3(e.exp(),vars)
            return (l**r)
        case AEPlus():
            l = ae2z3(e.left(),vars)
            r = ae2z3(e.right(),vars)
            return (l + r)
        case AEMinus():
            l = ae2z3(e.left(),vars)
            r = ae2z3(e.right(),vars)
            return (l - r)
        case AEMult():
            l = ae2z3(e.left(),vars)
            r = ae2z3(e.right(),vars)
            return (l * r)

''' The function [spec2z3] transforms a specification
    built using the [Spec] class hierarchy into the 
    corresponding format accepted by the Z3 theorem
    prover. '''

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

''' The function [prove_vcs] creates a solver instance
    in Z3, pushes all the verification conditions passed
    as arguments, negates them, and asks Z3 to provide a 
    model that satisfies them. ** Note ** to prove that the
    specifications are valid (an thus the program is correct)
    the answer of Z3 must be [unsat], that is, there exists no
    valuation to variables that makes the negation of the 
    formulas true; hence the formulas themselves must be theorems, 
    i.e., they are always true.'''

def prove_vcs(vcs,vars):
    s = Solver()
    for vc in vcs:
        # We negate each of the formulae so that if Z3 says unsat
        # then we know it is a theorem.
        s.add(Not(spec2z3(vc,vars)))
    print(s)
    return s.check()
