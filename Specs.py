from colorama import init, Fore, Back, Style
from Exprs import *

init(autoreset=True)

''' The classes below define the constructions
    of the syntax that allow to represent assertions.
    Recall that assertions are the logical version of
    Boolean expressions and that they are needed to
    write pre and post conditions, as well as invariants.'''

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

    def __eq__(self,other):
        match other:
            case SVal():
                return (self.__value == other.value())
            case _:
                return False

    def __hash__(self):
        return 1

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

    def __eq__(self,other):
        match other:
            case SNeg():
                return (self.__value == other.value())
            case _:
                return False

    def __hash__(self):
        return 2

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

    def __eq__(self,other):
        match other:
            case SImp():
                return (self.__lspec == other.left() and self.__rspec == other.right())
            case _:
                return False

    def __hash__(self):
        return 3

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

    def __eq__(self,other):
        match other:
            case SAnd():
                return (self.__lspec == other.left() and self.__rspec == other.right())
            case _:
                return False

    def __hash__(self):
        return 4

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

    def __eq__(self,other):
        match other:
            case SOr():
                return (self.__lspec == other.left() and self.__rspec == other.right())
            case _:
                return False

    def __hash__(self):
        return 5

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

    def __eq__(self,other):
        match other:
            case SEq():
                return (self.__lspec == other.left() and self.__rspec == other.right())
            case _:
                return False

    def __hash__(self):
        return 6


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

    def __eq__(self,other):
        match other:
            case SLt():
                return (self.__lspec == other.left() and self.__rspec == other.right())
            case _:
                return False
    
    def __hash__(self):
        return 7


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

    def __eq__(self,other):
        match other:
            case SGt():
                return (self.__lspec == other.left() and self.__rspec == other.right())
            case _:
                return False

    def __hash__(self):
        return 8


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

    def __eq__(self,other):
        match other:
            case SLeq():
                return (self.__lspec == other.left() and self.__rspec == other.right())
            case _:
                return False

    def __hash__(self):
        return 9


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

    def __eq__(self,other):
        match other:
            case SGeq():
                return (self.__lspec == other.left() and self.__rspec == other.right())
            case _:
                return False

    def __hash__(self):
        return 10

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


class VSubst_Exception(Exception):
    pass

''' Below you find a function that performs variable 
    substitutions in logical assertions. This is
    necessary for correctly compute weakest pre-conditions
    and also verification conditions.'''

def spec_subst(s,v,e):

    ''' This function substitutes the variable [v] by
        the expression [e] in the arithmetic expression 
        given by [s]. '''

    def aesubst(ae,v,e):

        ''' Substitution function for arithmetic expressions '''

        match ae:
            case AEVal():
                return ae
            case AEVar():
                if ae.name() == v:
                    return e
                else:
                    return ae
            case AEPlus():
                l = aesubst(ae.left(),v,e)
                r = aesubst(ae.right(),v,e)
                return AEPlus(l,r)
            case AEMinus(): 
                l = aesubst(ae.left(),v,e)
                r = aesubst(ae.right(),v,e)
                return AEMinus(l,r)
            case AEMult():
                l = aesubst(ae.left(),v,e)
                r = aesubst(ae.right(),v,e)
                return AEMult(l,r)
            case AEPow():
                l = aesubst(ae.base(),v,e)
                r = aesubst(ae.exp(),v,e)
                return AEPow(l,r)
            case _:
                raise VSubst_Exception

    ''' This function substitutes the variable [v] by
        the expression [e] in the Boolean expression 
        given by [s]. '''

    def besubst(be,v,e):

        ''' Substitution function for Boolean expressions '''

        match be:
            case SVal():
                return be
            case SNeg():
                return SNeg(besubst(be.value(),v,e))
            case SAnd() as f:
                l = besubst(be.left(),v,e)
                r = besubst(be.right(),v,e)
                return SAnd(l,r)
            case SOr():
                l = besubst(be.left(),v,e)
                r = besubst(be.right(),v,e)
                return SOr(l,r)
            case SEq():
                l = aesubst(be.left(),v,e)
                r = aesubst(be.right(),v,e)
                return SEq(l,r)
            case SLt():
                l = aesubst(be.left(),v,e)
                r = aesubst(be.right(),v,e)
                return SLt(l,r)
            case SGt():
                l = aesubst(be.left(),v,e)
                r = aesubst(be.right(),v,e)
                return SGt(l,r)
            case SLeq():
                l = aesubst(be.left(),v,e)
                r = aesubst(be.right(),v,e)
                return SLeq(l,r)
            case SGeq():
                l = aesubst(be.left(),v,e)
                r = aesubst(be.right(),v,e)
                return SGeq(l,r)
            case _:
                raise VSubst_Exception

    ''' Main body: selects the type of expression of [s]
        based on its type (if it is an instance of the class
        [AExpr], or [BExpr] otherwise), and calls the 
        suitable substitution function ([aesubst] or [besubst], 
        respectively). '''

    if isinstance(s,AExpr):
        return aesubst(s,v,e)
    else:
        return besubst(s,v,e)

''' Function that converts a Boolean expression
        into its specification counterpart.'''

def bexpr2spec(e):

    match e:
        case BEVal():
            return SVal(e.value())
        case BENeg():
            return SNeg(bexpr2spec(e.inner()))
        case BEAnd():
            l = bexpr2spec(e.left())
            r = bexpr2spec(e.right())
            return SAnd(l,r)
        case BEOr():
            l = bexpr2spec(e.left())
            r = bexpr2spec(e.right())
            return SOr(l,r)
        case BEEq():
            return SEq(e.left(),e.right())
        case BELt():
            return SLt(e.left(),e.right())
        case _:
            raise Spec_Exception
