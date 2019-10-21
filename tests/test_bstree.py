from bstree import BSTreeList, BSTreeNode
import unittest


class TestCase(unittest.TestCase):

    def test_get(self):
        colors = BSTreeList()
        assert colors.get(4) is None
        colors.set(9, 'Z')
        node = colors.get(9)
        assert type(node) == BSTreeNode

    def test_set(self):
        letters = BSTreeList()
        letters.set(9, 'Z')
        letters.set(6, 'A')
        letters.set(3, 'G')
        letters.set(4, 'F')
        assert letters.set(1, 'L') == 5

    def test_delete(self):
        pass

    def test_find_minimum(self):
        pass

    def test_replace_node_in_parent(self):
        pass

    def test_list(self):
        pass
