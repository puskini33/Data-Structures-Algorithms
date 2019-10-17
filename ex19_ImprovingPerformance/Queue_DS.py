"""
Author: Elena Hirjoaba
Date: 26.09.2019
"""


class QueueNode(object):
    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f'[{self.value}, {repr(nval)}, {repr(pval)}]'


class Queue(object):

    def __init__(self):
        """A list has a head, a tail and can be counted from both directions."""
        self.head = None
        self.tail = None

    def _invariant(self):
        if self.head:
            assert self.head.prev is None
            if self.head.next is None:
                assert self.head == self.tail
        if self.tail:
            assert self.tail.next is None
        if self.head is None:
            assert self.tail is None

    def shift(self, obj: str):
        """Appends the node at the tail of the queue."""
        node = QueueNode(obj, None, None)
        if self.head is None:
            self.head = node
            self.tail = self.head
            self._invariant()
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self._invariant()

    def pop(self) -> str:
        """Removes the node from the head of the queue and returns the value of the returned node."""
        if self.head is None:
            assert self.tail is None
            self._invariant()
            return None
        elif self.head == self.tail:
            removed_value = self.head.value
            self.head = None
            self.tail = None
            self._invariant()
            return removed_value
        else:
            removed_value = self.head.value
            self.head = self.head.next
            self.head.prev = None
            self._invariant()
            return removed_value

    def head_node(self) -> None or str:
        """Returns the value of the head node."""
        if self.head is None:
            return None
        else:
            return self.head.value

    def tail_node(self) -> None or str:
        """Returns the value of the tail node."""
        if self.tail is None:
            assert self.head is None
            return None
        else:
            return self.tail.value

    def count(self) -> int:
        """Returns the number of nodes in the queue."""
        node = self.head
        count = 0

        while node:
            count += 1
            node = node.next

        return count

    def empty(self) -> str:
        """Indicates if the queue is empty."""
        if self.head is None:
            return 'The queue is empty'
        else:
            return 'The queue is not empty'

    def dump(self, mark: str) -> str:
        """Dumps the contents of the queue."""
        if self.head is None:
            return 'There are no nodes in the queue to print'
        else:
            node = self.tail
            print(mark)

            while node:
                print(node, ' ', end='')
                node = node.next

            print()
