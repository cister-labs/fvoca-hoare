from colorama import init, Fore, Back, Style
from Exprs import *

init(autoreset=True)

class Spec:
    pass

class Spec_Exception(Exception):
    pass

class SAtom(Spec):

    ''' An atom is a Boolean expression. This is the
        base case for our specification language '''

    def __init__(self,be):
        self.__atom = be

    def bexpr(self):
        return self.__atom

    def __str__(self):
        return str(self.__atom)

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
        return "(" + str(self.__lspec) + Fore.MAGENTA + " ==> " + Style.RESET_ALL + str(self.__rspec) + ")"

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
        else:
            raise VSubst_Exception

    def besubst(be,v,e):

        ''' Substitution function for Boolean expressions '''

        if isinstance(be,BEVal):
            return be
        elif isinstance(be,BENeg):
            return BENeg(besubst(be.inner(),v,e))
        elif isinstance(be,BEAnd):
            l = besubst(be.inner_l(),v,e)
            r = besubst(be.inner_r(),v,e)
            return BEAnd(l,r)
        elif isinstance(be,BEOr):
            l = besubst(be.inner_l(),v,e)
            r = besubst(be.inner_r(),v,e)
            return BEOr(l,r)
        elif isinstance(be,BEEq):
            l = aesubst(be.inner_l(),v,e)
            r = aesubst(be.inner_r(),v,e)
            return BEEq(l,r)
        elif isinstance(be,BELt):
            l = aesubst(be.inner_l(),v,e)
            r = aesubst(be.inner_r(),v,e)
            return BELt(l,r)
        else:
            raise VSubst_Exception

    ''' Main body: selects the type of expression
        and proceeds with the right substitution
        function. '''

    if isinstance(s,AExpr):
        return aesubst(s,v,e)
    else:
        return besubst(s,v,e)
