class FuncDef(object):

    def __init__(self, name, params):
        self.name = name
        self.params = params

    def __repr__(self):
        return f'FUNCDEF{self.name, self.params}'


class FuncCall(object):

    def __init__(self, name, params):
        self.name = name
        self.params = params

    def __repr__(self):
        return f'FUNCCALL{self.name, self.params}'

class Parameters(object):

    def __init__(self, params):
        self.params = params

    def __repr__(self):
            return f'PARAMETERS: {self.params}'

class Integer(object):

    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return f'INTEGER: {self.number}'

class Plus(object):

    def __init__(self, plus, left, right):
        self.plus = plus
        self.left = left
        self.right = right

    def __repr__(self):
        return f'left: {self.left} {self.plus} right: {self.right}'
