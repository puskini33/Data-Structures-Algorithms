from analyzer import *

class Interpreter(object):

    def __init__(self, analyzed_tree, world_state):
        self.analyzed_tree = analyzed_tree
        self.world_state = world_state

    def interpret(self):
        print()
        print('Results of interpreter are: ')
        print()
        for node in self.analyzed_tree:
            node.interpret(self.world_state)
