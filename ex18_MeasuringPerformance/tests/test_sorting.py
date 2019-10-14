import sorting
from DoubleLinkedList import *
from random import randint
import unittest

max_numbers = 800


class TestCase(unittest.TestCase):

    def random_list(self, count) -> 'DoubleLinkedList':
        numbers = DoubleLinkedList()
        for i in range(count, 0, -1):
            numbers.shift(randint(0, 1000))  # adds nodes to the double linked list
        return numbers

    def is_sorted(self, numbers: 'DoubleLinkedList') -> bool:
        node = numbers.begin  # first node in the list
        while node and node.next:
            if node.value > node.next.value:  # check if current node is bigger than next node
                return False
            else:
                node = node.next

            return True

    def test_bubble_sort(self):
        numbers = self.random_list(max_numbers)  # a list is generated

        sorting.bubble_sort(numbers)  # call the bubble_sort function with the randomly generated list as a parameter

        assert self.is_sorted(numbers)  # verify that the bubble_sort function worked

    def test_merge_sort(self):
        numbers = self.random_list(max_numbers)  # a randomly generated list is created

        sorting.merge_sort(numbers)  # call the merge_ sort function with the newly randomly created list as parameter

        assert self.is_sorted(numbers)  # verify that the merge_sort function worked

    def test_quick_sort(self):
        numbers = self.random_list(max_numbers)  # a randomly generated list is created
        sorting.quick_sort(numbers, 0, numbers.count() - 1)

        assert self.is_sorted(numbers)

    def test_insertSort(self):
        numbers = self.random_list(max_numbers)  # a randomly generated list is created
        sorting.insertSort(numbers, numbers.count())

        assert self.is_sorted(numbers)


if __name__ == '__main__':
    speed = TestCase()
    speed.test_quick_sort()
    speed.test_merge_sort()
    speed.test_quick_sort()
    speed.test_insertSort()
    unittest.main(verbosity=2)
