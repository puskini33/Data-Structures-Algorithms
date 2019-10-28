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
        assert letters.root.key == 9
        assert letters.root.value == 'Z'
        letters.set(9, 'A')
        assert letters.root.value == 'A'
        letters.set(3, 'G')
        assert letters.root.left.value == 'G'

    def test_delete(self):
        letters = BSTreeList()
        letters.set(9, 'Z')
        letters.delete(9)
        assert letters.root is None
        letters.set(9, 'Z')
        letters.set(10, 'A')
        letters.set(3, 'C')
        assert letters.root.right
        assert letters.root.left
        letters.delete(3)
        assert letters.root.left is None
        letters.set(11, 'D')
        letters.set(13, 'F')
        letters.set(18, 'W')
        letters.set(33, 'Q')
        letters.delete(11)

    def test_list(self):
        pass
