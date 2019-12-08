class Production(object):
    def analyze(self, world):
        """Implement your analyzer here."""


class FuncDef(Production):

    def __init__(self, name, params):
        self.name = name
        self.params = params

    def __repr__(self):
        return f'FUNCDEF{self.name, self.params}'

    def analyze(self, world_state):
        world_state.add_function(self.name)
        print('FuncDef ', self.name)
        self.params.analyze(world_state)


class FuncBody(Production):

    def __init__(self, name, params):
        self.name = name
        self.params = params

    def __repr__(self):
        return f'   FUNCBODY: {self.name, self.params}'

    def analyze(self, world_state):
        world_state.add_function(self.name)
        print(f'FuncBody ', self.name)
        self.params.analyze(world_state)


class FuncCall(Production):

    def __init__(self, name, params):
        self.name = name
        self.params = params

    def __repr__(self):
        return f'FUNCCALL{self.name, self.params}'

    def analyze(self, world_state):
        print(f'FuncCall {self.name}')
        self.params.analyze(world_state)


class Parameters(Production):

    def __init__(self, params):
        self.params = params

    def __repr__(self):
            return f'PARAMETERS: {self.params}'

    def analyze(self, world_state):
        print('>> Parameters are: ', )
        for expr in self.params:
            expr.analyze(world_state)


class Expressions(Production):
    pass  # it simply passes to the next class


class Name(Production):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Name: {self.name}'

    def analyze(self, world_state):
        world_state.add_variable(self.name)
        print(f'NAME: {self.name}')


class Integer(Production):

    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return f'INTEGER: {self.number}'

    def analyze(self, world_state):
        print(f'INTEGER: {self.number}')


class Plus(Production):

    def __init__(self, plus, left, right):
        self.plus = plus
        self.left = left
        self.right = right

    def __repr__(self):
        return f'left: {self.left} + {self.plus} right: {self.right}'

    def analyze(self, world_state):
        print(f'left: {self.left.analyze(world_state)} {self.plus} right: {self.right.analyze(world_state)}')


class Equal(Production):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        print('Equality: ')
        return f'{self.left} = {self.right}'

    def analyze(self, world_state):
        print(f'EQUALITY: {self.left} = {self.right}')
