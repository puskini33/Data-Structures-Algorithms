from sys import exit


class Production(object):
    def analyze(self, world):
        """Implement your analyzer here."""

    def interpret(self, world):
        """Implement interpreter here."""


class FuncDef(Production):

    def __init__(self, name, params, body):
        self.name = name[1]
        self.params = params
        self.body = body

    def __repr__(self):
        return f'FUNCDEF({self.name}({self.params}): \t {self.body})'

    def call(self, world, params):
        params = params or Parameters()

        scope = world.clone()
        for i, p in enumerate(self.params.expressions):
            scope.variables[p.name] = params.expressions[i]

        for line in self.body:
            line.interpret(scope)

    def analyze(self, world_state):
        world_state.functions[self.name] = self


class FuncCall(Production):

    def __init__(self, name, params):
        self.name = name[1]
        self.params = params

    def __repr__(self):
        return f'\n\nFUNCCALL({self.name}({self.params}))'

    def analyze(self, world_state):
        try:
            if self.name in world_state.functions:
                self.params.analyze(world_state)
        except KeyError:
            print('Syntax Error: Undefined function. Function cannot be called.')
            exit(1)

    def interpret(self, world_state):
        funcdef = world_state.functions.get(self.name)
        funcdef.call(world_state, self.params)


class Parameters(Production):

    def __init__(self, params):
        self.expressions = params

    def __repr__(self):
            return f'PARAMETERS: {self.expressions}'

    def analyze(self, world_state):
        for expr in self.expressions:
            expr.analyze(world_state)

    def interpret(self, world_state):
        return [x.interpret(world_state) for x in self.expressions]


class Expressions(Production):
    pass


class Name(Expressions):

    def __init__(self, name):
        self.name = name[1]

    def __repr__(self):
        return f'NameExpr({self.name})'

    def analyze(self, world_state):
        world_state.variables[self.name] = self

    def interpret(self, world_state):
        ref = world_state.variables.get(self.name)
        return ref.interpret(world_state)


class Integer(Expressions):

    def __init__(self, number):
        self.number = int(number[1])

    def __repr__(self):
        return f'IntExpr({self.number})'

    def interpret(self, world_state):
        return self.number


class Addition(Expressions):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f'AddExpr({self.left}, {self.right})'

    def analyze(self, world_state):
        self.left.analyze(world_state)
        self.right.analyze(world_state)

    def interpret(self, world_state):
        return self.left.interpret(world_state) + self.right.interpret(world_state)


class Equal(Expressions):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Equality({self.left}, {self.right})'

    def interpret(self, world_state):
        print(f'EQUALITY: {self.left} = {self.right}')


class PrintFuncDef(Production):

    def call(self, world, params):
        print(*params.interpret(world))
