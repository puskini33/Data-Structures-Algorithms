from parser_format import Parser
from Scanner import Scanner
import grammar_productions as Rule
from analyzer import WorldState, Analyzer


class Runner(object):

    def __init__(self, local_parser):
        """Algorithm uses left most derivation to do the syntax analysis of the list of tokens from Scanner and outputs
        a parse tree."""
        self.local_parser = local_parser  # the Parser object is passed

    def root(self):
        """root = *(funccal / funcdef)"""
        first = self.local_parser.peek()  # peek at first element in the list_tokens of local scanner

        if first == 'DEF':  # if the token list starts with DEF
            return self.function_definition()  # it is a function definition; call function
        elif first == 'INDENT':  # if the next element is NAME
            self.local_parser.match('INDENT')
            return self.func_body()
        elif first == 'NAME':
            return self.function_call(first)

    def function_definition(self):
        """funcdef = DEF name LPAREN params RPAREN COLON body
        I ignore body for this example because that is hard.
        I mean, so you can learn how to do it."""

        self.local_parser.skip('DEF')  # discard def

        name = self.local_parser.match('NAME')  # matches NAME in the code

        self.local_parser.match('LPAREN')  # matches LPAREN in the code

        params = self.parameters()  # list of parameters

        self.local_parser.match('RPAREN')  # matches RPAREN

        self.local_parser.match('COLON')  # matches COLON

        return Rule.FuncDef(name, params)

    def parameters(self):
        """params = expression *(COMMA expression)"""
        params = []
        start = self.local_parser.peek()  # peek at current element
        while start != 'RPAREN':  # while start is not RPAREN
            params.append(self.expression())  # append first parameter, append second parameter
            start = self.local_parser.peek()  # peek at next element

            if start != 'RPAREN':  # if RPAREN is not reached yet, so there must be another parameter
                self.local_parser.match('COMMA')  # match COMMA and pop it

        return Rule.Parameters(params)  # return parameters

    def function_call(self, name):
        """funccall = name LPAREN params RPAREN"""

        name = self.local_parser.match('NAME')  # peek at the next element

        self.local_parser.match('LPAREN')  # match LPAREN and pop token

        params = self.parameters()  # list of parameters of the function

        self.local_parser.match('RPAREN')  # match RPAREN and pop token

        func_call_repr = Rule.FuncCall(name, params)
        return func_call_repr

    def func_body(self):
        name = self.local_parser.match('NAME')  # peek at the next element

        self.local_parser.match('LPAREN')  # match LPAREN and pop token

        params = self.parameters()  # list of parameters of the function

        self.local_parser.match('RPAREN')  # match RPAREN and pop token

        func_body_repr = Rule.FuncBody(name, params)
        return func_body_repr

    def expression(self):
        """expression = name / plus /integer"""
        start = self.local_parser.peek()  # peek at current element
        try:
            if start == 'NAME':  # if it is a name
                name = self.local_parser.match('NAME')
                name_repr =   Rule.Name(name)
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
        except SyntaxError:
            print('Syntax error %r' % start)

    def plus(self, left):
        """plus = expression PLUS expression"""
        plus = self.local_parser.match('PLUS')  # match + and pop PLUS token
        right = self.expression()  # get the right element of the addition
        plus_repr = Rule.Plus(plus, left, right)
        return plus_repr

    def main(self):
        results = []
        try:
            while not self.local_parser.done():
                results.append(self.root())  # go 1 time, 2 times, 3 times
        except LookupError:
            print('Index Error Exception Raised, list index out of range"')
        else:
            return results


code = ["def hello(x, y):", "    pprint(x + y)", "hello(10, 20)"]

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
            ((r"\s"),                      "SPACE")]

first_scanner = Scanner(TOKENS, code)
first_parser = Parser(first_scanner)
trial = Runner(first_parser)
local_runner = trial.main()
print(local_runner)

variables = {}
general_state = WorldState(variables)
local_analyzer = Analyzer(local_runner, general_state)
local_analyzer.analyze()
