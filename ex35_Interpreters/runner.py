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

    def _invariant(self, match):
        print(f'Syntax Error: Invalid Syntax: {match[1]}')
        exit(1)

    def root(self):
        """root = *(funccal / funcdef)"""
        first = self.local_parser.peek()  # peek at first element in the list_tokens of local scanner

        if first[0] == 'DEF':  # if the token list starts with DEF
            return self.function_definition()  # it is a function definition; call function
        elif first[0] == 'NAME':
            return self.function_call(first)
        else:
            self._invariant(first)

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

        body_repr = self.func_body()

        return Rule.FuncDef(name, params, body_repr)

    def parameters(self):
        """params = expression *(COMMA expression)"""
        params = []
        start = self.local_parser.peek()  # peek at current element
        while start[0] != 'RPAREN':  # while start is not RPAREN
            params.append(self.expression())  # append first parameter, append second parameter
            start = self.local_parser.peek()  # peek at next element

            if start[0] != 'RPAREN':  # if RPAREN is not reached yet, so there must be another parameter
                self.local_parser.match('COMMA')  # match COMMA and pop it

        return Rule.Parameters(params)  # return parameters

    def function_call(self, name):
        """funccall = name LPAREN params RPAREN"""

        name = self.local_parser.match('NAME')  # peek at the next element

        second = self.local_parser.peek()
        if second[0] == 'EQUAL':
            return self.equal(name)
        else:
            self.local_parser.match('LPAREN')  # match LPAREN and pop token

            params = self.parameters()  # list of parameters of the function

            self.local_parser.match('RPAREN')  # match RPAREN and pop token

            func_call_repr = Rule.FuncCall(name, params)
            return func_call_repr

    def func_body(self):
        while self.local_parser.match('INDENT'):
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
            if start[0] == 'NAME':  # if it is a name
                name = self.local_parser.match('NAME')
                name_repr = Rule.Name(name)
                if self.local_parser.peek()[0] == 'PLUS':  # if next element is PLUS
                    return self.plus(name_repr)  # as parameter is given the left side of the addition
                else:
                    return name_repr  # return name representation
            elif start[0] == 'INTEGER':  # if it is integer
                number = self.local_parser.match('INTEGER')  # match the integer and pop the token
                number_repr = Rule.Integer(number)

                if self.local_parser.peek()[0] == 'PLUS':  # if next token is PLUS
                    return self.plus(number_repr)  # as parameter is given the left argument of the addition
                else:
                    return number_repr
        except SyntaxError:
            print('Syntax error %r' % start)

    def plus(self, left):
        """plus = expression PLUS expression"""
        plus = self.local_parser.match('PLUS')  # match + and pop PLUS token
        right = self.expression()  # get the right element of the addition
        plus_repr = Rule.Addition(left, right)
        return plus_repr

    def equal(self, left):
        first_equal = self.local_parser.match('EQUAL')

        right = self.local_parser.match('INTEGER')

        plus = self.local_parser.peek()
        if plus[0] == 'PLUS':
            plus_repr = self.plus(right)
            return Rule.Equal(left, plus_repr)
        else:
            return 'ERROR'

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
        """This function implements scope.
        Remember “scope” is the idea that the
x, y in hello(x, y) do not impact an x or y variable you define outside the hello function."""
        temp = WorldState(self.variables.copy())
        temp.functions = self.functions
        return temp

    def add_variable(self, variable):
        if variable not in self.variables:
            self.variables['name'] = variable
        return

    def add_function(self, function):
        if function not in self.functions:
            self.functions['name'] = function
        return

    def check_existence_variable(self, variable_name):
        try:
            assert variable_name in self.variables
        except AssertionError:
            return 'DefinitionError: Variable is not defined.'

    def run_function(self, function_name):
        try:
            assert function_name in self.functions
        except AssertionError:
            return 'DefinitionError: Function not defined.'
        return function_name()



code = ["def hello(x, y):", "    pprint(x + y)", "hello(10, 14)"]

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
local_interpreter = Interpreter(analyzed_tree, general_state)
local_interpreter.interpret()
