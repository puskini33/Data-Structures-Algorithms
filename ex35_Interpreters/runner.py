from parser_format import Parser
from Scanner import Scanner
import grammar_productions as Rule
from analyzer import Analyzer
from interpreter import Interpreter
from sys import exit


class Runner(object):

    def __init__(self, local_parser):
        """Algorithm uses left most derivation to do the syntax analysis of the list of tokens from Scanner and outputs
        a parse tree."""
        self.local_parser = local_parser  # the Parser object is passed

    def _error(self, match):
        if not match or match == 'ERROR':
            print(f'Syntax Error during Parsing: Invalid Syntax')
            exit(1)
        else:
            return

    def root(self):
        """root = *(funccal / funcdef)"""
        first = self.local_parser.peek()  # peek at first element in the list_tokens of local scanner

        if first == 'DEF':  # if the token list starts with DEF
            return self.function_definition()  # it is a function definition; call function
        elif first == 'NAME':
            return self.function_call(first)
        else:  # if match is ERROR
            self._error(first)

    def function_definition(self):
        """funcdef = DEF name LPAREN params RPAREN COLON body
        I ignore body for this example because that is hard.
        I mean, so you can learn how to do it."""

        self.local_parser.skip('DEF')  # discard def

        name = self.local_parser.match('NAME')  # matches NAME in the code
        self._error(name)
        lparen = self.local_parser.match('LPAREN')  # matches LPAREN in the code
        self._error(lparen)
        params = self.parameters()  # list of parameters

        rparen = self.local_parser.match('RPAREN')  # matches RPAREN
        self._error(rparen)
        colon = self.local_parser.match('COLON')  # matches COLON
        self._error(colon)
        body_repr = self.function_body()

        return Rule.FuncDef(name, params, body_repr)

    def parameters(self):
        """params = expression *(COMMA expression)"""
        params = []
        start = self.local_parser.peek()  # peek at current element
        self._error(start)
        while start != 'RPAREN':  # while start is not RPAREN
            params.append(self.expression())  # append first parameter, append second parameter
            start = self.local_parser.peek()  # peek at next element
            self._error(start)
            if start != 'RPAREN':  # if RPAREN is not reached yet, so there must be another parameter
                comma = self.local_parser.match('COMMA')  # match COMMA and pop it
                self._error(comma)
        return Rule.Parameters(params)  # return parameters

    def function_call(self, name=0):
        """funccall = name LPAREN params RPAREN"""

        name = self.local_parser.match('NAME')  # peek at the next element
        self._error(name)
        second = self.local_parser.peek()
        self._error(second)
        if second == 'EQUAL':
            return self.equal(name)
        else:
            lparen = self.local_parser.match('LPAREN')  # match LPAREN and pop token
            self._error(lparen)
            params = self.parameters()  # list of parameters of the function

            rparen = self.local_parser.match('RPAREN')  # match RPAREN and pop token
            self._error(rparen)
            func_call_repr = Rule.FuncCall(name, params)
            return func_call_repr

    def function_body(self):
        body = []
        while self.local_parser.skip("INDENT"):
            body.append(self.function_call())
        return body

    def expression(self):
        """expression = name / plus /integer"""
        start = self.local_parser.peek()  # peek at current element
        self._error(start)

        if start == 'NAME':  # if it is a name
            name = self.local_parser.match('NAME')
            name_repr = Rule.Name(name)
            if self.local_parser.peek() == 'PLUS':  # if next element is PLUS
                return self.plus(name_repr)  # as parameter is given the left side of the addition
            else:
                return name_repr  # return name representation
        elif start == 'INTEGER':  # if it is integer
            number = self.local_parser.match('INTEGER')  # match the integer and pop the token
            number_repr = Rule.Integer(number)

            if self.local_parser.peek() == 'PLUS':  # if next token is PLUS
                return self.plus(number_repr)  # as parameter is given the left argument of the addition
            else:
                return number_repr

    def plus(self, left):
        """plus = expression PLUS expression"""
        plus = self.local_parser.match('PLUS')  # match + and pop PLUS token
        self._error(plus)
        right = self.expression()  # get the right element of the addition
        plus_repr = Rule.Addition(left, right)
        return plus_repr

    def equal(self, left):
        equal = self.local_parser.match('EQUAL')
        self._error(equal)
        right = self.local_parser.match('INTEGER')
        self._error(right)

        plus = self.local_parser.peek()
        self._error(plus)
        plus_repr = self.plus(right)
        return Rule.Equal(left, plus_repr)

    def main(self):
        results = []
        try:
            while not self.local_parser.done():
                results.append(self.root())  # go 1 time, 2 times, 3 times
        except LookupError:
            print('Index Error Exception Raised, list index out of range"')

        return results


class WorldState(object):

    def __init__(self, variables):
        self.variables = variables
        self.functions = {}
        self.functions['print'] = Rule.PrintFuncDef()

    def clone(self):
        """Sort of a lame way to implement scope."""
        temp = WorldState(self.variables.copy())
        temp.functions = self.functions
        return temp



code = ["def hello(x, y):", "    print(x + y)", "hello(10, 14)"]

TOKENS = [
            ((r"^def"),                    "DEF"),
            ((r"^[a-zA-Z_][a-zA-Z0-9_]*"), "NAME"),
            ((r"^[0-9]+"),                 "INTEGER"),
            ((r"^\("),                     "LPAREN"),
            ((r"^\)"),                     "RPAREN"),
            ((r"^\+"),                     "PLUS"),
            ((r"^:"),                      "COLON"),
            ((r"^,"),                      "COMMA"),
            ((r"((\s\s\s\s)|\t)"),         "INDENT"),
            ((r"\s"),                      "SPACE"),
            ((r"\="),                      "EQUAL")]


first_scanner = Scanner(TOKENS, code)
first_parser = Parser(first_scanner)
trial = Runner(first_parser)
parse_tree = trial.main()
print(parse_tree)


general_state = WorldState({})
local_analyzer = Analyzer(parse_tree, general_state)
analyzed_tree = local_analyzer.analyze()
print()
print('Result is: ')
for prod in analyzed_tree:
    prod.interpret(general_state)
