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

    def test_shift(self):
        colors = DoubleLinkedList()
        colors.shift("Cadium Orange")
        assert colors.count() == 1

        colors.shift("Carbazole Violet")
        assert colors.count() == 2

        colors.shift("Carbazole Yellow")
        assert colors.count() == 3

        assert colors.pop() == "Cadium Orange"
        assert colors.count() == 2
        assert colors.pop() == "Carbazole Violet"
        assert colors.count() == 1
        assert colors.pop() == "Carbazole Yellow"
        assert colors.count() == 0

    def test_unshift(self):
        colors = DoubleLinkedList()
        colors.shift('Viridian')
        colors.shift('Sap Green')
        colors.shift('Van Dyke')
        assert colors.unshift() == 'Van Dyke'
        assert colors.unshift() == 'Sap Green'
        assert colors.unshift() == 'Viridian'
        assert colors.unshift() is None

if __name__ == '__main__':
    unittest.main(verbosity=2)
