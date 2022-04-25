''' The following classes establish the base concepts
    from which complete grammars for arithmetic and boolean
    expressions will be defined. Moreover, exceptions are 
    also defined to ensure correct creation of the expressions.'''

class AExpr:
    pass

class AExpr_Exception(Exception):
    pass

class BExpr:
    pass

class BExpr_Exception(Exception):
    pass

''' The following classes represent the various 
    constructs of arithmetic expressions. '''

class AEVar(AExpr):
    ''' Class that represents an integer variable '''

    def __init__(self,n):
        if not(type(n) == str):
            raise AExpr_Exception
        self.__name = n

    def name(self):
        return self.__name

    def __str__(self):
        return str(self.__name)

class AEVal(AExpr):

    ''' Class that represents an integer value '''

    def __init__(self,v):
        if not(type(v) == int):
            raise AExpr_Exception
        self.__value = v

    def value(self):
        return self.__value

    def __str__(self):
        return str(self.__value)

class AEPlus(AExpr):

    ''' Class that represents the sum of two
        arithmetic expressions.'''

    def __init__(self,l,r):
        if not (isinstance(l,AExpr) or isinstance(r,AExpr)):
            raise AExpr_Exception
        self.__rnode   = r
        self.__lnode   = l

    def inner_l(self):
        return self.__lnode

    def inner_r(self):
        return self.__rnode

    def __str__(self):
        return '('+str(self.__lnode)+'+'+str(self.__rnode)+')'

class AEMinus(AExpr):

    ''' Class that represents the subtraction
        of two arithmetic expressions.'''

    def __init__(self,l,r):
        if not (isinstance(l,AExpr) or isinstance(r,AExpr)):
            raise AExpr_Exception
        self.__rnode   = r
        self.__lnode   = l

    def inner_l(self):
        return self.__lnode

    def inner_r(self):
        return self.__rnode

    def __str__(self):
        return '('+str(self.__lnode)+'-'+str(self.__rnode)+')'

class AEMult(AExpr):

    ''' Class that represents the multiplication
        of two arithmetic expressions.'''

    def __init__(self,l,r):
        if not (isinstance(l,AExpr) or isinstance(r,AExpr)):
            raise AExpr_Exception
        self.__rnode   = r
        self.__lnode   = l

    def inner_l(self):
        return self.__lnode

    def inner_r(self):
        return self.__rnode

    def __str__(self):
        return '('+str(self.__lnode)+'*'+str(self.__rnode)+')'

class AEPow(AExpr):

    ''' Build the power of an expression [e] up to an
        integer [n].'''

    def __init__(self,e,i):
        if not (isinstance(e,AExpr) or isinstance(i,AExpr)):
            raise AExpr_Exception    
        self.__base = e
        self.__exp  = i
    
    def base(self):
        return self.__base

    def exp(self):
        return self.__exp

    def __str__(self):
        return str(self.__base)+' ^ '+str(self.__exp)

''' The following classes represent the various 
    constructs of Boolean expressions. '''

class BEVal(BExpr):

    def __init__(self,v):
        if not(type(v) == bool):
            raise BExpr_Exception
        self.__val = v

    def value(self):
        return self.__val

    def __str__(self):
        return str(self.__val)

class BENeg(BExpr):

    def __init__(self,be):
        if not isinstance(be,BExpr):
            raise BExpr_Exception
        self.__inner = be

    def inner(self):
        return self.__inner

    def __str__(self):
        return "~("+str(self.__inner)+")"

class BEAnd(BExpr):

    ''' Class that represents the conjunction
        of two Boolean expressions.'''

    def __init__(self,l,r):
        if not (isinstance(l,BExpr) or isinstance(r,BExpr)):
            raise BExpr_Exception
        self.__lnode   = l
        self.__rnode   = r

    def inner_l(self):
        return self.__lnode

    def inner_r(self):
        return self.__rnode

    def __str__(self):
        return "("+str(self.__lnode)+(u' ⋀ ')+str(self.__rnode)+")"

class BEOr(BExpr):

    ''' Class that represents the disjunction
        of two Boolean expressions.'''

    def __init__(self,l,r):
        if not (isinstance(l,BExpr) or isinstance(r,BExpr)):
            raise BExpr_Exception
        self.__lnode   = l
        self.__rnode   = r

    def inner_l(self):
        return self.__lnode

    def inner_r(self):
        return self.__rnode

    def __str__(self):
        return "("+str(self.__lnode)+u' ⋁ '+str(self.__rnode)+")"


class BEEq(BExpr):

    ''' Class that represents the equality
        of two arithmetic expressions.'''

    def __init__(self,l,r):
        if not (isinstance(l,AExpr) or isinstance(r,AExpr)):
            raise BExpr_Exception
        self.__lnode   = l
        self.__rnode   = r

    def inner_l(self):
        return self.__lnode

    def inner_r(self):
        return self.__rnode

    def __str__(self):
        return "("+str(self.__lnode)+" == "+str(self.__rnode)+")"


class BELt(BExpr):

    ''' Class that represents the less-than
        relation between two arithmetic expressions.'''

    def __init__(self,l,r):
        if not (isinstance(l,AExpr) or isinstance(r,AExpr)):
            raise BExpr_Exception
        self.__lnode   = l
        self.__rnode   = r

    def inner_l(self):
        return self.__lnode

    def inner_r(self):
        return self.__rnode

    def __str__(self):
        return "("+str(self.__lnode)+" < "+str(self.__rnode)+")"

class BEGt(BExpr):

    ''' Class that represents the less-than
        relation between two arithmetic expressions.'''

    def __init__(self,l,r):
        if not (isinstance(l,AExpr) or isinstance(r,AExpr)):
            raise BExpr_Exception
        self.__lnode   = l
        self.__rnode   = r

    def inner_l(self):
        return self.__lnode

    def inner_r(self):
        return self.__rnode

    def __str__(self):
        return "("+str(self.__lnode)+" > "+str(self.__rnode)+")"

class BELeq(BExpr):

    ''' Class that represents the less-than
        relation between two arithmetic expressions.'''

    def __init__(self,l,r):
        if not (isinstance(l,AExpr) or isinstance(r,AExpr)):
            raise BExpr_Exception
        self.__lnode   = l
        self.__rnode   = r

    def inner_l(self):
        return self.__lnode

    def inner_r(self):
        return self.__rnode

    def __str__(self):
        return "("+str(self.__lnode)+u' ⩽ '+str(self.__rnode)+")"

class BEGeq(BExpr):

    ''' Class that represents the less-than
        relation between two arithmetic expressions.'''

    def __init__(self,l,r):
        if not (isinstance(l,AExpr) or isinstance(r,AExpr)):
            raise BExpr_Exception
        self.__lnode   = l
        self.__rnode   = r

    def inner_l(self):
        return self.__lnode

    def inner_r(self):
        return self.__rnode

    def __str__(self):
        return "("+str(self.__lnode)+u' ⩾ '+str(self.__rnode)+")"


