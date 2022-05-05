from colorama import init, Fore, Back, Style
from Exprs import *

init(autoreset=True)

class Command:
    pass

class Skip(Command):

    def __eq__(self,other):
        match other:
            case Skip():
                return True
            case _:
                return False

class Assgn(Command):

    def __init__(self,v,e):
        self.__vname = v
        self.__expr  = e

    def name(self):
        return self.__vname

    def value(self):
        return self.__expr

    def __eq__(self,other):
        match other:
            case Assgn():
                if self.__vname == other.name() and self.__expr == other.value():
                    return True
                else:
                    return False
            case _:
                return False

    def __str__(self):
        return str(self.__vname) + " "+ Fore.GREEN + ":= " + Style.RESET_ALL + str(self.__expr) + " ;"

class Seq(Command):

    def __init__(self,cl,cr):
        self.__cl = cl
        self.__cr = cr

    def left(self):
        return self.__cl

    def right(self):
        return self.__cr

    def __eq__(self,other):
        match other:
            case Seq():
                return ((self.__cl == other.left()) and 
                        (self.__cr == other.right()))
            case _:
                return False

    def __str__(self):
        return (str(self.__cl) + str(self.__cr))

class IfThen(Command):

    def __init__(self,b,ct,cf):
        self.__cond = b
        self.__ct   = ct
        self.__cf   = cf

    def cond(self):
        return self.__cond

    def left(self):
        return self.__ct

    def right(self):
        return self.__cf
    
    def __eq__(self,other):
        match other:
            case IfThen():
                return ((self.__cond == other.cond()) and
                        (self.__ct == other.left()) and 
                        (self.__cf == other.right()))
            case _:
                return False

    def __str__(self):
        b  = Fore.GREEN + "If" + "(" + str(self.__cond) + ") "
        ls = Fore.GREEN + "then" + " { " + str(self.__ct) + " }"
        rs = Fore.GREEN + "else" + " { " + str(self.__ct) + " }"
        return  (b + ls + rs)  
    
class While(Command):

    def __init__(self,b,i,c):
        self.__cond = b
        self.__inv  = i
        self.__body = c

    def cond(self):
        return self.__cond

    def inv(self):
        return self.__inv

    def body(self):
        return self.__body

    def __eq__(self,other):
        match other:
            case Seq():
                return ((self.__cond == other.cond()) and 
                        (self.__inv == other.inv()) and
                        (self.__body == other.body())
                        )
            case _:
                return False

    def __str__(self):
        b  = Fore.GREEN + "While" + Style.RESET_ALL + "(" + str(self.__cond) + ") "
        i  = Fore.CYAN + " { " + str(self.__inv) + " } " + Style.RESET_ALL
        return (b + i + "{ " + str(self.__body) + " }")
