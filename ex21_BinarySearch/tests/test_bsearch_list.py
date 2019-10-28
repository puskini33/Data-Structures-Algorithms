from bsearch_list import *
import unittest


class TestCase(unittest.TestCase):

    def test_find_number(self):
        manual_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        assert find_number(19, manual_list) == 19
        assert find_number(1, manual_list) == 1
        assert find_number(13, manual_list) == 13
