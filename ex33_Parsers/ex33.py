from Scanner import *
from pprint import pprint


def root(tokens):
    """root = *(funccal / funcdef)"""
    first = Scanner.peek(tokens)  # returns first token that could be matched

    if first == 'DEF':
        return function_definition(tokens)
    elif first == 'NAME':
        name = Scanner.match(tokens, 'NAME')
        second = Scanner.peek(tokens)
        if second == 'LPAREN':
            return function_call(tokens, name)
        else:
            assert False, 'Not a FUNCDEF or FUNCCALL'


def function_definition(tokens):
    """funcdef = DEF name LPAREN params RPAREN COLON body
    I ignore body for this example because that is hard.
    I mean, so you can learn how to do it."""

    Scanner.skip(tokens)  # discard def
    name = Scanner.match(tokens, 'NAME')
    Scanner.match(tokens, 'LPAREN')
    params = parameters (tokens)
    Scanner.match(tokens, 'RPAREN')
    Scanner.match(tokens, 'COLON')
    return {'type': 'FUNCDEF', 'name': name, 'params': params}


def parameters(tokens):
    """params = expression *(COMA expression)"""
    params = []
    start = Scanner.peek(tokens)
    while start != 'RPAREN':
        params.append(expression(tokens))
        start = Scanner.peek(tokens)
        if start != 'RPAREN':
            assert Scanner.match(tokens, 'COMMA')
    return params


def function_call(tokens, name):
    """funccall = name LPAREN params RPAREN"""
    Scanner.match(tokens, 'LPAREN')
    params = parameters(tokens)
    Scanner.match(tokens, 'RPAREN')
    return {'type': 'FUNCCALL', 'name': name, 'params': parameters}


def expression(tokens):
    """expression = name / plus /integer"""
    start = Scanner.peek(tokens)

    if start == 'NAME':
        name = Scanner.match(tokens, 'NAME')
        if Scanner.peek(tokens) == 'PLUS':
            return plus(tokens, name)
        else:
            return name
    elif start == 'INTEGER':
        number = Scanner.match(tokens, 'INTEGER')
        if Scanner.peek(tokens) == 'PLUS':
            return plus(tokens, number)
        else:
            return number
    else:
        assert False, 'Syntax error %r' % start


def plus(tokens, left):
    """plus = expression PLUS expression"""
    Scanner.match(tokens, 'PLUS')
    right = expression(tokens)
    return {'type': 'PLUS', 'left': left, 'right': right}


def main(tokens):
    results = []
    while tokens:
        results.append(root(tokens))
    return results


parsed = main(Scanner.scan())
pprint(parsed)
