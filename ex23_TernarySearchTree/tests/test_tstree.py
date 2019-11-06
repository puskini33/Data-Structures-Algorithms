from tstree import *
import unittest


class TestCase(unittest.TestCase):

    def test_get(self):
        fruits = TSTree()
        fruits.set('banana', 11)
        fruits.set('apple', 10)
        fruits.set('orange', 14)
        assert fruits.get('orange') == 14
        assert fruits.get('apple') == 10

    def test_find_all(self):
        fruits = TSTree()
        fruits.set('banana', 0)
        fruits.set('apple', 11)
        fruits.set('application', 6)
        results = [n.key for n in fruits.find_all('appl')]
        assert results == ['apple', 'application']

    def test_find_shortest(self):
        fruits = TSTree()
        fruits.set('apple', 11)
        fruits.set('application', 10)
        assert fruits.find_shortest('appl').key == 'apple'

    def test_find_longest(self):
        fruits = TSTree()
        fruits.set('apple', 11)
        fruits.set('application', 10)
        assert fruits.get('application') == 10
        assert fruits.find_longest('appl').key == 'application'

    def test_find_part(self):
        fruits = TSTree()
        fruits.set('apple', 11)
        fruits.set('application', 10)
        assert fruits.find_part('appl').key == 'apple'