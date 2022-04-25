from distutils.util import subst_vars
from Exprs import *
from Imp   import *
from Specs import *

class WPRec_Exception(Exception):
    pass


def wprec(c,q):

    if isinstance(c,Skip):
        return q
    elif isinstance(c,Assgn):
        return spec_subst(q,c.name(),c.value())
    elif isinstance(c,Seq):
        r = wprec(c.right(),q)
        return wprec(c.left(),r)
    elif isinstance(c,IfThen):
        l = SImp(bexpr2spec(c.cond()),wprec(c.left(),q))
        r = SImp(bexpr2spec(BENeg(c.cond())),wprec(c.right(),q))
        return SAnd(l,r)
    elif isinstance(c,While):
        return c.inv()
    else:
        raise WPRec_Exception


