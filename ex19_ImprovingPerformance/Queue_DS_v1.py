"""
Author: Elena Hirjoaba
Date: 10.17.2019
Changes: upgraded pop(), shift(), head(), tail(); deleted count()
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
        self.count = 0

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
        if self.tail is None:  # no node
            self.tail = QueueNode(obj, None, None)
            self.head = self.tail
        else:  # at least 1 node
            node = QueueNode(obj, None, self.tail)
            self.tail.next = node
            self.tail = node

        self.count += 1

    def pop(self) -> str:
        """Removes the node from the head of the queue and returns the value of the returned node."""
        if self.head:  # at least 1 node
            removed_value = self.head.value

            if self.head == self.tail:  # 1 node
                self.head = None
                self.tail = None
            else:  # more than 1 node
                self.head = self.head.next
                self.head.prev = None

            self.count -= 1
            return removed_value

        else:  # no node
            return None

    def head_node(self) -> None or str:
        """Returns the value of the head node."""
        return self.head and self.head.value or None

    def tail_node(self) -> None or str:
        """Returns the value of the tail node."""
        return self.tail and self.tail.value or None

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
