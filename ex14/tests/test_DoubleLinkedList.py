from DoubleLinkedList import DoubleLinkedList
import unittest


class TestCase(unittest.TestCase):

    def test_push(self):
        colors = DoubleLinkedList()
        colors._invariant()
        colors.push('Pthalo Blue')
        assert colors.count() == 1
        colors.push('Ultramarine Bleu')
        assert colors.count() == 2
        colors.push('Magenta')
        assert colors.count() == 3
        colors.push('Green')
        assert colors.count() == 4
        colors.push('Red')
        assert colors.count() == 5
        colors._invariant()

    def test_pop(self):
        colors = DoubleLinkedList()
        colors.push("Magenta")
        colors._invariant()
        colors.push("Alizarin")
        colors.push("Van Dyke")
        colors._invariant()
        assert colors.pop() == "Van Dyke"
        colors._invariant()
        # assert colors.get(1) == "Alizarin"
        assert colors.pop() == "Alizarin"
        assert colors.pop() == "Magenta"
        colors._invariant()
        assert colors.pop() is None


if __name__ == '__main__':
    unittest.main(verbosity=2)
