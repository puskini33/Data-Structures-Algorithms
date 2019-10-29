from bsearch_list import *
import unittest


class TestCase(unittest.TestCase):

    def test_find_number(self):
        man_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        assert find_number(19, man_list) == 19
        assert find_number(1, man_list) == 1
        assert find_number(13, man_list) == 13
        assert find_number(23, man_list) is None
