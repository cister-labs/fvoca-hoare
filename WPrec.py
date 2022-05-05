from Exprs import *
from Imp   import *
from Specs import *

class WPRec_Exception(Exception):
    pass

''' The first function that you need to implement. It
    refers to the function that implements the
    weakest precondition generation, given a code block
    [c] and a specification [q] (that serves the role of
    post condition.'''

def wprec(c,q):

    # First, we analyse what type of program instruction
    # we have, and then write the corresponding code.
    match c:
        case Skip():
            # Fill the code here
            return q
        case Assgn():
            # Fill the code here
            return spec_subst(q,c.name(),c.value())
        case Seq():
            # Fill the code here
            return wprec(c.left(),wprec(c.right(),q))
        case IfThen():
            # Fill the code here
            l = SImp(bexpr2spec(c.cond()),wprec(c.left(),q))
            r = SImp(bexpr2spec(BENeg(c.cond())),wprec(c.right(),q))
            return SAnd(l,r)
        case While():
            # Fill the code here
            return c.inv()
        case _:
            # This is the case that will not be reached, but is here
            # for completeness.
            raise WPRec_Exception




