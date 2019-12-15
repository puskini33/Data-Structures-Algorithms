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
        return f'FUNCDEF({self.name}({self.params}): {self.body})'

    def call(self, world, params):
        params = params or Parameters(params)

        scope = world.clone()
        for i, p in enumerate(self.params.expressions):
            scope.variables[p.name] = params.expressions[i]

        for line in self.body:
            line.interpret(scope)

    def analyze(self, world_state):
        world_state.functions[self.name] = self
        self.params.analyze(world_state)

    def interpret(self, world_state):  # where should this step go
        self.params.interpret(world_state)


class FuncBody(Production):

    def __init__(self, name, params):
        self.name = name[1]
        self.params = params

    def __repr__(self):
        return f'\n    FUNCBODY({self.name}({self.params}))'


class FuncCall(Production):

    def __init__(self, name, params):
        self.name = name[1]
        self.params = params

    def __repr__(self):
        return f'\n\nFUNCCALL({self.name}({self.params}))'

    def analyze(self, world_state):
        self.params.analyze(world_state)

    def interpret(self, world_state):
        # funcdef = world_state.functions[self.name]
        # funcdef.call(world_state, self.params)

        self.params.interpret(world_state)


class Parameters(Production):

    def __init__(self, params):
        self.params = params

    def __repr__(self):
            return f'PARAMETERS: {self.params}'

    def analyze(self, world_state):
        for expr in self.params:
            expr.analyze(world_state)

    def interpret(self, world_state):
        for expr in self.params:
            expr.interpret(world_state)


class Expressions(Production):
    pass


class Name(Expressions):

    def __init__(self, name):
        self.name = name[1]

    def __repr__(self):
        return f'NameExpr({self.name})'

    def analyze(self, world_state):
        pass

    def interpret(self, world_state):
        print(f'NAME: {self.name}')


class Integer(Expressions):

    def __init__(self, number):
        self.number = number[1]

    def __repr__(self):
        return f'IntExpr({self.number})'

    # def analyze(self, world_state):
        # print(f'INTEGER: {self.number}')

    def interpret(self, world_state):
        print(f'INTEGER: {self.number}')


class Addition(Expressions):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f'AddExpr({self.left}, {self.right})'

    def analyze(self, world_state):
        self.left.analyze()
        self.right.analyze()

    def interpret(self, world_state):  # where should this step go
        print(f'{self.left} + {self.right} = ')
        result = f'{self.left} + {self.right}'
        print(result)


class Equal(Expressions):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Equality({self.left}, {self.right})'

    # def analyze(self, world_state):
        # print(f'EQUALITY: {self.left} = {self.right}')

    def interpret(self, world_state):
        print(f'EQUALITY: {self.left} = {self.right}')


class PrintFuncDef(Production):

    def call(self, world, params):
        print(*params.interpret(world))
