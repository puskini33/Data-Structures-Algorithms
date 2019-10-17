from Queue_DS import Queue
import unittest

"""
Author: Elena Hirjoaba
Date: 10.17.2019
"""


class TestCase(unittest.TestCase):

    def test_shift(self):
        for i in range(0, 800):
            colors = Queue()
            colors.shift('Red')
            assert colors.count == 1
            colors.shift('Blue')
            assert colors.count == 2

    def test_pop(self):
        for i in range(0, 800):
            colors = Queue()
            colors.shift('Red')
            colors.dump('before blue')
            colors.shift('Blue')
            colors.dump('after blue')
            colors.shift('Yellow')
            assert colors.pop() == 'Red'
            assert colors.pop() == 'Blue'
            assert colors.pop() == 'Yellow'

    def test_head_node(self):
        for i in range(0, 800):
            colors = Queue()
            assert colors.head_node() is None
            colors.shift('Red')
            assert colors.head_node() == 'Red'
            colors.shift('Blue')
            assert colors.head_node() == 'Red'

    def test_tail_node(self):
        for i in range(0, 800):
            colors = Queue()
            assert colors.tail_node() is None
            colors.shift('Red')
            assert colors.tail_node() == 'Red'
            colors.shift('Blue')
            assert colors.tail_node() == 'Blue'

    def test_empty(self):
        for i in range(0, 800):
            colors = Queue()
            assert colors.empty() == 'The queue is empty'
            colors.shift('Red')
            assert colors.empty() == 'The queue is not empty'
            colors.shift('Blue')
            assert colors.empty() == 'The queue is not empty'


if __name__ == '__main__':
    speed = TestCase()
    speed.test_pop()
    speed.test_shift()
    speed.test_empty()
    speed.test_head_node()
    speed.test_tail_node()
    unittest.main(verbosity=2)
