from sarray_binary_tree import *
import unittest


class TestCase(unittest.TestCase):

    def test_find_shortest(self):
        fruits = SuffixArray('banana')
        assert fruits.find_shortest('a') == 5
        assert fruits.find_shortest('l') == -1
        assert fruits.find_shortest('c') == -1

    def test_find_longest(self):
        fruit = SuffixArray('banana')
        assert fruit.find_longest('na') == 2
        assert fruit.find_longest('a') == 1
        assert fruit.find_longest('c') == -1

    def test_find_all(self):
        fruit = SuffixArray('banana')
        assert fruit.find_all('a') == [('a', 5), ('ana', 3), ('anana', 1)]
        assert fruit.find_all('c') == (-1, -1)

