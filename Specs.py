from colorama import init, Fore, Back, Style
from Exprs import *

init(autoreset=True)

class Spec:
    pass

class Spec_Exception(Exception):
    pass

class SVal(Spec):

    ''' An atom is a Boolean expression. This is the
        base case for our specification language '''

    def __init__(self,b):
        if not (type(b) == bool):
            raise Spec_Exception
        self.__value = b

    def value(self):
        return self.__value

    def __str__(self):
        return Fore.MAGENTA + str(self.__value) + Style.RESET_ALL

class SNeg(Spec):

    ''' An atom is a Boolean expression. This is the
        base case for our specification language '''

    def __init__(self,b):
        if not (isinstance(b,Spec)):
            raise Spec_Exception
        self.__value = b

    def value(self):
        return self.__value

    def __str__(self):
        return Fore.MAGENTA + u'~' + Style.RESET_ALL + "(" + str(self.__value) +")" 

class SImp(Spec):

    ''' Build and implication between two
        specifications. '''

    def __init__(self,sl,sr):
        self.__lspec = sl
        self.__rspec = sr

    def left(self):
        return self.__lspec

    def right(self):
        return self.__rspec

    def __str__(self):
        return "(" + str(self.__lspec) + Fore.MAGENTA + u' -> ' + Style.RESET_ALL + str(self.__rspec) + ")"

class SAnd(Spec):

    ''' Build and implication between two
        specifications. '''

    def __init__(self,sl,sr):
        self.__lspec = sl
        self.__rspec = sr

    def left(self):
        return self.__lspec

    def right(self):
        return self.__rspec

    def __str__(self):
        return "(" + str(self.__lspec) + Fore.MAGENTA + u' ⋀ ' + Style.RESET_ALL + str(self.__rspec) + ")"

class SOr(Spec):

    ''' Build and implication between two
        specifications. '''

    def __init__(self,sl,sr):
        self.__lspec = sl
        self.__rspec = sr

    def left(self):
        return self.__lspec

    def right(self):
        return self.__rspec

    def __str__(self):
        return "(" + str(self.__lspec) + Fore.MAGENTA + u' ⋁ ' + Style.RESET_ALL + str(self.__rspec) + ")"

class SEq(Spec):

    ''' Build and implication between two
        specifications. '''

    def __init__(self,sl,sr):
        if isinstance(sl,AExpr) and isinstance(sr,AExpr):
            self.__lspec = sl
            self.__rspec = sr
        else:
            raise Spec_Exception

    def left(self):
        return self.__lspec

    def right(self):
        return self.__rspec

    def __str__(self):
        return "(" + str(self.__lspec) + Fore.MAGENTA + " == " + Style.RESET_ALL + str(self.__rspec) + ")"

class SLt(Spec):

    ''' Build an less-than relation between two
        specifications. '''

    def __init__(self,sl,sr):
        if isinstance(sl,AExpr) and isinstance(sr,AExpr):
            self.__lspec = sl
            self.__rspec = sr
        else:
            raise Spec_Exception

    def left(self):
        return self.__lspec

    def right(self):
        return self.__rspec

    def __str__(self):
        return "(" + str(self.__lspec) + Fore.MAGENTA + " < " + Style.RESET_ALL + str(self.__rspec) + ")"

class SGt(Spec):

    ''' Build an less-than relation between two
        specifications. '''

    def __init__(self,sl,sr):
        if isinstance(sl,AExpr) and isinstance(sr,AExpr):
            self.__lspec = sl
            self.__rspec = sr
        else:
            raise Spec_Exception

    def left(self):
        return self.__lspec

    def right(self):
        return self.__rspec

    def __str__(self):
        return "(" + str(self.__lspec) + Fore.MAGENTA + " > " + Style.RESET_ALL + str(self.__rspec) + ")"

class SLeq(Spec):

    ''' Build an less-than relation between two
        specifications. '''

    def __init__(self,sl,sr):
        if isinstance(sl,AExpr) and isinstance(sr,AExpr):
            self.__lspec = sl
            self.__rspec = sr
        else:
            raise Spec_Exception

    def left(self):
        return self.__lspec

    def right(self):
        return self.__rspec

    def __str__(self):
        return "(" + str(self.__lspec) + Fore.MAGENTA + u' ⩽ ' + Style.RESET_ALL + str(self.__rspec) + ")"

class SGeq(Spec):

    ''' Build an less-than relation between two
        specifications. '''

    def __init__(self,sl,sr):
        if isinstance(sl,AExpr) and isinstance(sr,AExpr):
            self.__lspec = sl
            self.__rspec = sr
        else:
            raise Spec_Exception

    def left(self):
        return self.__lspec

    def right(self):
        return self.__rspec

    def __str__(self):
        return "(" + str(self.__lspec) + Fore.MAGENTA + u' ⩾ ' + Style.RESET_ALL + str(self.__rspec) + ")"

class SForall(Spec):

    ''' Build a universaly quantified formula. '''

    def __init__(self,v,s):
        self.__var = v
        self.__spec = s

    def var(self):
        return self.__var

    def spec(self):
        return self.__spec

    def __str__(self):
        return (u'∀' + (str(self.__var) + ", " + str(self.__spec)))

class SEx(Spec):

    ''' Build an existentially quantified formula. '''

    def __init__(self,v,s):
        self.__var = v
        self.__spec = S

    def var(self):
        return self.__var

    def spec(self):
        return self.__spec

    def __str__(self):
        return (u'∃' + (str(self.__var) + ", " + str(self.__spec)))


''' Below you find a function that performs variable 
    substitutions in logical assertions. This is
    necessary for correctly compute weakest pre-conditions
    and also verification conditions.'''

class VSubst_Exception(Exception):
    pass


def spec_subst(s,v,e):

    def aesubst(ae,v,e):

        ''' Substitution function for arithmetic expressions '''

        if isinstance(ae,AEVal):
            return ae
        elif isinstance(ae,AEVar):
            if ae.name() == v:
                return e
            else:
                return ae
        elif isinstance(ae,AEPlus):
            l = aesubst(ae.inner_l(),v,e)
            r = aesubst(ae.inner_r(),v,e)
            return AEPlus(l,r)
        elif isinstance(ae,AEMinus):
            l = aesubst(ae.inner_l(),v,e)
            r = aesubst(ae.inner_r(),v,e)
            return AEMinus(l,r)
        elif isinstance(ae,AEMult):
            l = aesubst(ae.inner_l(),v,e)
            r = aesubst(ae.inner_r(),v,e)
            return AEMult(l,r)
        elif isinstance(ae,AEPow):
            l = aesubst(ae.base(),v,e)
            r = aesubst(ae.exp(),v,e)
            return AEPow(l,r)
        else:
            raise VSubst_Exception

    def besubst(be,v,e):

        ''' Substitution function for Boolean expressions '''

        if isinstance(be,SVal):
            return be
        elif isinstance(be,SNeg):
            return SNeg(besubst(be.value(),v,e))
        elif isinstance(be,SAnd):
            l = besubst(be.left(),v,e)
            r = besubst(be.right(),v,e)
            return SAnd(l,r)
        elif isinstance(be,SOr):
            l = besubst(be.left(),v,e)
            r = besubst(be.right(),v,e)
            return SOr(l,r)
        elif isinstance(be,SEq):
            l = aesubst(be.left(),v,e)
            r = aesubst(be.right(),v,e)
            return SEq(l,r)
        elif isinstance(be,SLt):
            l = aesubst(be.left(),v,e)
            r = aesubst(be.right(),v,e)
            return SLt(l,r)
        elif isinstance(be,SGt):
            l = aesubst(be.left(),v,e)
            r = aesubst(be.right(),v,e)
            return SGt(l,r)
        elif isinstance(be,SLeq):
            l = aesubst(be.left(),v,e)
            r = aesubst(be.right(),v,e)
            return SLeq(l,r)
        elif isinstance(be,SGeq):
            l = aesubst(be.left(),v,e)
            r = aesubst(be.right(),v,e)
            return SGeq(l,r)
        else:
            raise VSubst_Exception

    ''' Main body: selects the type of expression
        and proceeds with the right substitution
        function. '''

    if isinstance(s,AExpr):
        return aesubst(s,v,e)
    else:
        return besubst(s,v,e)

def bexpr2spec(e):

    ''' Function that converts a Boolean expression
        into its specification counterpart.'''

    if isinstance(e,BEVal):
        return SVal(e.value())
    elif isinstance(e,BENeg):
        return SNeg(bexpr2spec(e.inner()))
    elif isinstance(e,BEAnd):
        l = bexpr2spec(e.inner_l())
        r = bexpr2spec(e.inner_r())
        return SAnd(l,r)
    elif isinstance(e,BEOr):
        l = bexpr2spec(e.inner_l())
        r = bexpr2spec(e.inner_r())
        return SOr(l,r)
    elif isinstance(e,BEEq):
        return SEq(e.inner_l(),e.inner_r())
    elif isinstance(e,BELt):
        return SLt(e.inner_l(),e.inner_r())
    else:
        raise Spec_Exception
