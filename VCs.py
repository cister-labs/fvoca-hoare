from pyparsing import empty
from Exprs import *
from Imp   import *
from Specs import *
from WPrec import *

class VC_Exception(Exception):
    pass

''' Ineficient version of the VC generation algorithm. This is the
    second block of code that you have to implement. '''

def VC(pre,c,post):
    # Like the case of the function [wprec], the way the code goes
    # is by first analysing what kind of command instruction we
    # are looking at, and then provide the corresponding code as
    # defined in the mathematical definition of the VC function
    match c:
        case Skip():
            # This part is "offered"
            return { SImp(pre,post) }
        case Assgn():
            # Enter your code here
            return { SImp(pre,spec_subst(post,c.name(),c.value())) }
        case Seq():
            # This part is "offered"
            i = wprec(c.right(),post)
            l = VC(pre,c.left(),i)
            r = VC(i,c.right(),post)
            return l.union(r)
        case IfThen():
            # Enter your code here
            pre_pos = SAnd(pre,bexpr2spec(c.cond()))
            pre_neg = SAnd(pre,bexpr2spec(BENeg(c.cond())))
            l = VC(pre_pos,c.left(),post)
            r = VC(pre_neg,c.right(),post)
            return l.union(r)
        case While():
            # Enter your code here
            s = { SImp(pre,c.inv()) , SImp(SAnd(c.inv(),bexpr2spec(BENeg(c.cond()))),post) }
            return s.union(
                VC(
                    SAnd(pre,bexpr2spec(BENeg(c.cond()))),
                    c.body(),
                    post
                )
            )
        case _:
            raise VC_Exception


''' Improved version of the VC generation algorithm.
    This is the final block of code that you have to
    implement. The approach for doing it is the same
    as the one used in the previous two function [wprec]
    and [VC].'''

def VCG(pre,c,post):
    
    def VC_i(p,pst):
        match p:
            case Skip():
                # Enter your code here
                return set()
            case Assgn():
                # Enter your code here
                return set()
            case Seq():
                # Enter your code here
                l = VC_i(p.left(),wprec(p.right(),pst))
                r = VC_i(p.right(),pst)
                return l.union(r)
            case IfThen():
                # Enter your code here
                l = VC_i(p.left(),pst)
                r = VC_i(p.right(),pst)
                return l.union(r)
            case While():
                # Enter your code here
                i = { SImp(SAnd(p.inv(),bexpr2spec(p.cond())),wprec(p.body(),p.inv())) }
                j = { SImp(SAnd(p.inv(),SNeg(bexpr2spec(p.cond()))),pst) }
                r = VC_i(p.body(),p.inv())
                return i.union(j.union(r))

    # For your convenience, we left implemented the call entry point of
    # the [VCG] function, which willl then call the function [VC_i] that
    # must be completed above.
    r = { SImp(pre,wprec(c,post)) }
    return r.union(VC_i(c,post))
