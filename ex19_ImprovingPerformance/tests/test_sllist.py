from sllist import SingleLinkedList
import unittest


class TestClass(unittest.TestCase):

    def test_push(self):
        for i in range(0, 800):
            colors = SingleLinkedList()
            colors.push('Pthalo Blue')
            assert colors.count == 1
            colors.push('Ultramarine Bleu')
            assert colors.count == 2
            colors.push('Magenta')
            assert colors.count == 3
            colors.push('Green')
            assert colors.count == 4
            colors.push('Red')
            assert colors.count == 5

    def test_pop(self):
        for i in range(0, 800):
            colors = SingleLinkedList()
            colors.push('Magenta')
            colors.push('Alizarin')
            colors.push('Blue')
            assert colors.pop() == 'Blue'
            assert colors.pop() == 'Alizarin'
            assert colors.pop() == 'Magenta'
            assert colors.pop() is None

    def test_shift(self):
        for i in range(0, 800):
            colors = SingleLinkedList()
            colors.shift("Cadium Orange")
            assert colors.count == 1

            colors.shift("Carbazole Violet")
            assert colors.count == 2

            assert colors.pop() == "Cadium Orange"
            assert colors.count == 1
            assert colors.pop() == "Carbazole Violet"
            assert colors.count == 0

    def test_unshift(self):
        for i in range(0, 800):
            colors = SingleLinkedList()
            colors.push('Viridian')
            colors.push('Sap Green')
            colors.push('Van Dyke')
            assert colors.unshift() == 'Viridian'
            assert colors.unshift() == 'Sap Green'
            assert colors.unshift() == 'Van Dyke'
            assert colors.unshift() is None

    def test_remove(self):
        for i in range(0, 800):
            colors = SingleLinkedList()
            colors.push('Cobalt')
            colors.push('Zinc White')
            colors.push('Nickle Yellow')
            colors.push('Perinone')
            colors.remove('Nickle Yellow')
            assert colors.count == 3
            # colors.dump('before perinone')
            colors.remove('Perinone')
            assert colors.count == 2
            # colors.dump('after perinone')
            colors.remove('Zinc White')
            assert colors.count == 1

    def test_first(self):
        for i in range(0, 800):
            colors = SingleLinkedList()
            colors.push('Cadmium Red Light')
            assert colors.first() == 'Cadmium Red Light'
            colors.push('Hansa Yellow')
            assert colors.first() == 'Cadmium Red Light'
            colors.shift('Pthalo Green')
            assert colors.first() == 'Pthalo Green'

    def test_last(self):
        for i in range(0, 800):
            colors = SingleLinkedList()
            colors.push('Cadmium Red Light')
            assert colors.last() == 'Cadmium Red Light'
            colors.push('Hansa Yellow')
            assert colors.last() == 'Hansa Yellow'
            colors.shift('Pthalo Green')
            assert colors.last() == 'Hansa Yellow'

    def test_get(self):
        for i in range(0, 800):
            colors = SingleLinkedList()
            colors.push('Vermillion')
            assert colors.get(0) == 'Vermillion'
            colors.push('Sap Green')
            assert colors.get(0) == 'Vermillion'
            assert colors.get(1) == 'Sap Green'
            colors.push('Cadmium Yellow Light')
            assert colors.get(0) == 'Vermillion'
            assert colors.get(1) == 'Sap Green'
            assert colors.get(2) == 'Cadmium Yellow Light'
            assert colors.pop() == 'Cadmium Yellow Light'
            assert colors.get(0) == 'Vermillion'
            assert colors.get(1) == 'Sap Green'
            assert colors.get(2) is None
            colors.pop()
            assert colors.get(0) == 'Vermillion'
            colors.pop()
            assert colors.get(0) is None


if __name__ == '__main__':
    speed = TestClass()
    speed.test_pop()
    speed.test_push()
    speed.test_get()
    speed.test_shift()
    speed.test_unshift()
    speed.test_first()
    speed.test_last()
    unittest.main(verbosity=2)
