from parser_format import Parser
from Scanner import Scanner
from pprint import pprint
import re


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
        elif first == 'NAME':  # if the next element is NAME
            name = self.local_parser.match('NAME')  # match the name of the function and pop token
            second = self.local_parser.peek()  # peek at the next element
            if second == 'LPAREN':  # if next element is left parenthesis
                return self.function_call(name)  # this code follows the pattern of a function call
            else:
                assert False, 'Not a FUNCDEF or FUNCCALL'

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
        return {'type': 'FUNCDEF', 'name': name, 'params': params}  # print the analyzed syntax in a specific format

    def parameters(self):
        """params = expression *(COMMA expression)"""
        params = []
        start = self.local_parser.peek()  # peek at current element
        while start != 'RPAREN':  # while start is not RPAREN
            params.append(self.expression())  # append first parameter, append second parameter
            start = self.local_parser.peek()  # peek at next element
            if start != 'RPAREN':  # if RPAREN is not reached yet, so there must be another parameter
                assert self.local_parser.match('COMMA')  # match COMMA and pop it
        return params  # return parameters

    def function_call(self, name):
        """funccall = name LPAREN params RPAREN"""
        self.local_parser.match('LPAREN')  # match LPAREN and pop token
        params = self.parameters()  # list of parameters of the function
        self.local_parser.match('RPAREN')  # match RPAREN and pop token
        return {'type': 'FUNCCALL', 'name': name, 'params': params}

    def expression(self):
        """expression = name / plus /integer"""
        start = self.local_parser.peek()  # peek at current element

        if start == 'NAME':  # if it is a name
            name = self.local_parser.match('NAME')  # match NAME and pops it
            if self.local_parser.peek() == 'PLUS':  # if next element is PLUS
                return self.plus(name)  # as parameter is given the left side of the addition
            else:
                return name  # return name
        elif start == 'INTEGER':  # if it is integer
            number = self.local_parser.match('INTEGER')  # match the integer and pop the token
            if self.local_parser.peek() == 'PLUS':  # if next token is PLUS
                return self.plus(number)  # as parameter is given the left argument of the addition
            else:
                return number
        else:
            assert False, 'Syntax error %r' % start

    def plus(self, left):
        """plus = expression PLUS expression"""
        self.local_parser.match('PLUS')  # match + and pop PLUS token
        right = self.expression()  # get the right element of the addition
        return {'type': 'PLUS', 'left': left, 'right': right}

    def main(self):
        results = []
        while not self.local_parser.done():
            results.append(self.root())  # go 1 time, 2 times, 3 times
        return results


code = ["def hello(x, y):", "    print(x + y)", "hello(10, 20)"]

TOKENS = [
        (re.compile(r"^def"),                    "DEF"),
        (re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*"), "NAME"),
        (re.compile(r"^[0-9]+"),                 "INTEGER"),
        (re.compile(r"^\("),                     "LPAREN"),
        (re.compile(r"^\)"),                     "RPAREN"),
        (re.compile(r"^\+"),                     "PLUS"),
        (re.compile(r"^:"),                      "COLON"),
        (re.compile(r"^,"),                      "COMMA"),
        (re.compile(r"^\s+"),                    "INDENT")
]


first_scanner = Scanner(TOKENS, code)
print('List of tokens from lexical analyzer contains: ')
pprint(first_scanner.list_tokens)
first_parser = Parser(first_scanner)
trial = Runner(first_parser)
main = trial.main()
print()
print()
print('The parse tree from the syntactic analyzer is: ')
pprint(main)
