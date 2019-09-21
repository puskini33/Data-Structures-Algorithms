from sllist import SingleLinkedList
import unittest


class TestClass(unittest.TestCase):

    def test_push(self):
        colors = SingleLinkedList()
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

    def test_pop(self):
        colors = SingleLinkedList()
        colors.push('Magenta')
        colors.push('Alizarin')
        colors.push('Blue')
        assert colors.pop() == 'Blue'
        assert colors.pop() == 'Alizarin'
        assert colors.pop() == 'Magenta'
        assert colors.pop() is None

    def test_shift(self):
        colors = SingleLinkedList()
        colors.shift("Cadium Orange")
        assert colors.count() == 1

        colors.shift("Carbazole Violet")
        assert colors.count() == 2

        assert colors.pop() == "Cadium Orange"
        assert colors.count() == 1
        assert colors.pop() == "Carbazole Violet"
        assert colors.count() == 0

    def test_unshift(self):
        colors = SingleLinkedList()
        colors.push('Viridian')
        colors.push('Sap Green')
        colors.push('Van Dyke')
        assert colors.unshift() == 'Viridian'
        assert colors.unshift() == 'Sap Green'
        assert colors.unshift() == 'Van Dyke'
        assert colors.unshift() is None

    def test_remove(self):
        colors = SingleLinkedList()
        colors.push('Cobalt')
        colors.push('Zinc White')
        colors.push('Nickle Yellow')
        colors.push('Perinone')
        assert colors.remove('Cobalt') == 0
        colors.dump('before perinone')
        assert colors.remove('Perinone') == 2
        colors.dump('after perinone')
        assert colors.remove('Nickle Yellow') == 1
        assert colors.remove('Zinc White') == 0


if __name__ == '__main__':
    unittest.main(verbosity=2)
