from Exprs import *
from Imp   import *
from Specs import *
from WPrec import *


class VC_Exception(Exception):
    pass


''' Ineficient version of the VC generation algorithm'''

def VC(pre,c,post):

    if isinstance(c,Skip):
        return { SImp(pre,post) }
    elif isinstance(c,Assgn):
        return { SImp(pre,spec_subst(post,c.name(),c.value())) }
    elif isinstance(c,Seq):
        i = wprec(c.right(),post)
        l = VC(pre,c.left(),i)
        r = VC(i,c.right(),post)
        return l.union(r)
    elif isinstance(c,IfThen):
        pre_pos = SAnd(pre,bexpr2spec(c.cond()))
        pre_neg = SAnd(pre,bexpr2spec(BENeg(c.cond())))
        l = VC(pre_pos,c.left(),post)
        r = VC(pre_neg,c.right(),post)
        return l.union(r)
    elif isinstance(c,While):
        s = { SImp(pre,c.inv()) , SImp(SAnd(c.inv(),bexpr2spec(BENeg(c.cond()))),post) }
        return s.union(
            VC(
                SAnd(pre,bexpr2spec(BENeg(c.cond()))),
                c.body(),
                post
            )
        )
    else:
        raise VC_Exception

''' Improved version of the VC generation algorithm'''

def VCG(pre,c,post):
    def VCi(c,post):
        pass
    pass