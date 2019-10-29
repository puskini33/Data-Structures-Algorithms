from bsearch_linked_list import *
import unittest


class TestCase(unittest.TestCase):

    def test_bsearch_ll(self):
        dll = DoubleLinkedList()
        for i in range(0, 21):
            dll.push(i)

        assert bsearch_ll(4, dll) == 4
        assert bsearch_ll(22, dll) is None
        assert bsearch_ll(1, dll) == 1
        assert bsearch_ll(0, dll) == 0
        assert bsearch_ll(20, dll) == 20
