"""
1. Give the PunyPyAnalyzer a parse tree, which are all Grammar Production Classes
2. Also give the PunyPyAnalyzer a state world(i.e., PunyPyWorld)"""


class Production(object):  # a Production class that all of my grammar productions will inherit from
    def analyze(self, world):  # world is the PunyPyWorld state
        """All grammar Productions inherit from here.
        Implement analyzer here"""


class FuncCall(Production):

    def __init__(self, name, params: 'Params Production Class'):
        self.name = name
        self.params = params

    def analyze(self, world):
        print("> FuncCall: ", self.name)
        self.params.analyze(world)


class Parameters(Production):

    def __init__(self, expressions):
        self.expressions = expressions

    def analyze(self, world):
        print(">> Parameters: ")
        for expr in self.expressions:
            expr.analyze(world)


class Expr(Production):
    pass


class IntExpr(Expr):
    def __init__(self, integer):
        self.integer = integer

    def analyze(self, world):
        print(">>>> IntExpr: ", self.integer)


class AddExpr(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def analyze(self, world):
        print(">>> AddExpr: ")
        self.left.analyze(world)
        self.right.analyze(world)


class PunyPyWorld(object):  # state of the world

    def __init__(self, variables):
        self.variables = variables  # fill this with functions: print etc.
        self.functions = {}


class PunyPyAnalyzer(object):   # take a parse tree and the world state and make the grammar productions run
    """Makes all the Grammar Productions run"""
    def __init__(self, parse_tree, world):
        self.parse_tree = parse_tree
        self.world = world  # PunyPyWorld object

    def analyze(self):
        for node in self.parse_tree:  # each node is a Grammar Production Rule
            node.analyze(self.world)  # call each GP Class's analyze(SELF.WORLD) method


variables = {}
world = PunyPyWorld(variables)
script = [FuncCall('hello',
                Parameters([
                    AddExpr(IntExpr(10), IntExpr(20))
                ]))]  # modify the indent to create this parse tree

analyzer = PunyPyAnalyzer(script, world)
analyzer.analyze()
