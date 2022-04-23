from colorama import init, Fore, Back, Style
from Exprs import *

init(autoreset=True)

class Command:
    pass

class Skip(Command):
    pass

class Assgn(Command):

    def __init__(self,v,e):
        self.__vname = v
        self.__expr  = e

    def name(self):
        return self.__vname

    def value(self):
        return self.__expr

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

    def __str__(self):
        b  = Fore.GREEN + "While" + "(" + str(self.__cond) + ") "
        i  = " { " + Fore.CYAN + str(self.__ct) + " }"
        return (b + ls + str(self.__body))