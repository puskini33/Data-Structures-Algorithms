from grammar_productions import *


class Analyzer(object):

    def __init__(self, parser_tree, world_state):
        self.parser_tree = parser_tree
        self.world_state = world_state

    def analyze(self):
        print()
        print('Results of analyzer are: ')
        print()
        for node in self.parser_tree:
            node.analyze(self.world_state)


class WorldState(object):

    def __init__(self, variables):
        self.variables = variables
        self.functions = {}
