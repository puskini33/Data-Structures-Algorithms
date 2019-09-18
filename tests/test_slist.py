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
        assert colors.pop() == 'Alizarin'
        assert colors.pop() == 'Magenta'
        assert colors.pop() is None


if __name__ == '__main__':
    unittest.main(verbosity=2)
