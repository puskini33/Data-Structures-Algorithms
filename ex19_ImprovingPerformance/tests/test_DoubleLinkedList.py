from DoubleLinkedList import DoubleLinkedList
import unittest

"""
Author: Elena Hirjoaba
Date: 26.09.2019
"""


class TestCase(unittest.TestCase):

    def test_push(self):
        for i in range(0, 800):
            colors = DoubleLinkedList()
            colors._invariant()
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
            colors._invariant()

    def test_pop(self):
        for i in range(0, 800):
            colors = DoubleLinkedList()
            colors.push("Magenta")
            colors._invariant()
            colors.push("Alizarin")
            colors.push("Van Dyke")
            colors._invariant()
            assert colors.pop() == "Van Dyke"
            colors._invariant()
            assert colors.get(1) == "Alizarin"
            assert colors.pop() == "Alizarin"
            assert colors.pop() == "Magenta"
            colors._invariant()
            assert colors.pop() is None

    def test_shift(self):
        for i in range(0, 800):
            colors = DoubleLinkedList()
            colors.shift("Cadium Orange")
            assert colors.count == 1

            colors.shift("Carbazole Violet")
            assert colors.count == 2

            colors.shift("Carbazole Yellow")
            assert colors.count == 3

            assert colors.pop() == "Cadium Orange"
            assert colors.count == 2
            assert colors.pop() == "Carbazole Violet"
            assert colors.count == 1
            assert colors.pop() == "Carbazole Yellow"
            assert colors.count == 0

    def test_unshift(self):
        for i in range(0, 800):
            colors = DoubleLinkedList()
            colors.shift('Viridian')
            colors.shift('Sap Green')
            colors.shift('Van Dyke')
            assert colors.unshift() == 'Van Dyke'
            assert colors.unshift() == 'Sap Green'
            assert colors.unshift() == 'Viridian'
            assert colors.unshift() is None

    def test_remove(self):
        for i in range(0, 800):
            colors = DoubleLinkedList()
            colors.push("Cobalt")
            colors.push("Zinc White")
            colors.push("Nickle Yellow")
            colors.push("Perinone")
            assert colors.remove("Cobalt") == 0
            colors._invariant()
            colors.dump("before perinone")
            assert colors.remove("Perinone") == 2
            colors._invariant()
            colors.dump("after perinone")
            assert colors.remove("Nickle Yellow") == 1
            colors._invariant()
            assert colors.remove("Zinc White") == 0
            colors._invariant()

    def test_first(self):
        for i in range(0, 800):
            colors = DoubleLinkedList()
            colors.push("Cadmium Red Light")
            assert colors.first() == "Cadmium Red Light"
            colors.push("Hansa Yellow")
            assert colors.first() == "Cadmium Red Light"
            colors.shift("Pthalo Green")
            assert colors.first() == "Pthalo Green"

    def test_last(self):
        for i in range(0, 800):
            colors = DoubleLinkedList()
            colors.push("Cadmium Red Light")
            assert colors.last() == "Cadmium Red Light"
            colors.push("Hansa Yellow")
            assert colors.last() == "Hansa Yellow"
            colors.shift("Pthalo Green")
            assert colors.last() == "Hansa Yellow"

    def test_get(self):
        for i in range(0, 800):
            colors = DoubleLinkedList()
            colors.push("Vermillion")
            assert colors.get(0) == "Vermillion"
            colors.push("Sap Green")
            assert colors.get(0) == "Vermillion"
            assert colors.get(1) == "Sap Green"
            colors.push("Cadmium Yellow Light")
            assert colors.get(0) == "Vermillion"
            assert colors.get(1) == "Sap Green"
            assert colors.get(2) == "Cadmium Yellow Light"
            assert colors.pop() == "Cadmium Yellow Light"
            assert colors.get(0) == "Vermillion"
            assert colors.get(1) == "Sap Green"
            assert colors.get(2) is None
            colors.pop()
            assert colors.get(0) == "Vermillion"
            colors.pop()
            assert colors.get(0) is None


if __name__ == '__main__':
    speed = TestCase()
    speed.test_pop()
    speed.test_unshift()
    speed.test_shift()
    speed.test_push()
    speed.test_get()
    speed.test_first()
    speed.test_last()
    speed.test_remove()
    unittest.main(verbosity=2)
