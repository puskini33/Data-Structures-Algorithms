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

    def add_variable(self, variable):
        if variable[1] not in self.variables:
            self.variables['name'] = variable
        return

    def add_function(self, function):
        if function[1] not in self.functions:
            self.functions['name'] = function
        return

    def check_existance_variable(self, variable_name):
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
