"""
Name: simple.py
Purpose: Simple language based on example from pyPEG

This example demonstrates grammar definition using python constructs.
It is taken and adapted from pyPEG project (see http://www.fdik.org/pyPEG/).
"""

from arpeggio import *
from arpeggio.export import PMDOTExport, PTDOTExport
from arpeggio import RegExMatch as _

def comment():          return [_("//.*"), _("/\*.*\*/")]
def literal():          return _(r'\d*\.\d*|\d+|".*?"')
def symbol():           return _(r"\w+")
def operator():         return _(r"\+|\-|\*|\/|\=\=")
def operation():        return symbol, operator, [literal, functioncall]
def expression():       return [literal, operation, functioncall]
def expressionlist():   return expression, ZeroOrMore(",", expression)
def returnstatement():  return Kwd("return"), expression
def ifstatement():      return Kwd("if"), "(", expression, ")", block, Kwd("else"), block
def statement():        return [ifstatement, returnstatement], ";"
def block():            return "{", OneOrMore(statement), "}"
def parameterlist():    return "(", symbol, ZeroOrMore(",", symbol), ")"
def functioncall():     return symbol, "(", expressionlist, ")"
def function():         return Kwd("function"), symbol, parameterlist, block
def simpleLanguage():   return function

try:
    import arpeggio
    arpeggio.DEBUG = True
    
    # Parser instantiation. simpleLanguage is root definition and comment is
    # grammar rule for comments.
    parser = ParserPython(simpleLanguage, comment)

    # We save parser model to dot file in order to visualise it.
    # We can make a jpg out of it using dot (part of graphviz) like this
    # dot -Tjpg -O simple_parser.dot
    PMDOTExport().exportFile(parser.parser_model,
            "simple_parser_model.dot")
    
    # Parser model for comments is handled as separate model
    PMDOTExport().exportFile(parser.comments_model,
            "simple_parser_comments.dot")
        
    input = """
        function fak(n) {
            if (n==0) {
                // For 0! result is 0
                return 0;
            } else { /* And for n>0 result is calculated recursively */
                return n * fak(n - 1);
            };
        }
    """
    parse_tree = parser.parse(input)
    
    PTDOTExport().exportFile(parse_tree,
            "simple_parse_tree.dot")
    
except NoMatch, e:
    print "Expected %s at position %s." % (e.value, str(e.parser.pos_to_linecol(e.position)))