from __future__ import unicode_literals, print_function
from pypeg2 import *

"""
/*****************************************************
Module Description: Here we define how a datatype looks like in izitag
/*****************************************************
"""

class StringLiteral(str):
     grammar = "'",word,"'"
    
     
     
class IntLiteral(str):
     grammar = re.compile(r"\d+")
     
    
class FloatLiteral(str):
    grammar= re.compile(r'(\d+(.\d+)?)')
    
class DataType(Keyword):
    grammar = Enum( K("int"), K("float") , K("String"))
    
    
stringToParse = " 99 "
f = parse(stringToParse, IntLiteral)
print(f)

stringToParse = "1.0"
f = parse(stringToParse, FloatLiteral)
print(f)

stringToParse = " 'ThisIsASingleString' "
f = parse(stringToParse, StringLiteral)
print(f)


stringToParse = " int  "
f = parse(stringToParse, DataType)
print(f)

stringToParse = " float  "
f = parse(stringToParse, DataType)
print(f)

stringToParse = " String  "
f = parse(stringToParse, DataType)
print(f)
