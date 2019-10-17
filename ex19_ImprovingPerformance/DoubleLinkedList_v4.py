"""
Author: Elena Hirjoaba
Date: 26.09.2019
Changes: count() is removed; push(); pop(); shift() and unshift()
"""


class DoubleLinkedListNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f'[{self.value}, {repr(nval)}, {repr(pval)}]'


def manually_introduce_nodes():
    node1 = DoubleLinkedListNode('Red', None, None)
    print(node1)
    node2 = DoubleLinkedListNode('Blue', node1, None)
    node1 = DoubleLinkedListNode('Red', None, node2)
    print(node1)
    print(node2)
    node3 = DoubleLinkedListNode('Orange', node2, None)
    node2 = DoubleLinkedListNode('Blue', node1, node3)
    print(node1)
    print(node2)
    print(node3)


class DoubleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None
        self.count = 0

    def _invariant(self):
        if self.begin is None:
            assert self.end is None
        elif self.begin.next is None:
            assert self.begin == self.end
        elif self.begin.next is not None:
            assert self.begin.prev is None
            assert self.end.next is None

    def push(self, obj: str):
        """Appends a new value at the end of the list."""
        if self.end:  # there is at least 1 node
            node = DoubleLinkedListNode(obj, None, self.end)
            self.end.next = node
            self.end = node
        else:  # there is more than 1 node
            self.begin = DoubleLinkedListNode(obj, None, None)
            self.end = self.begin

        self.count += 1

    def pop(self) -> str or None:
        """Removes the last item and returns it."""
        if self.end:  # there is at least 1 node
            value = self.end.value

            if self.end == self.begin:  # there is 1 node
                self.end = None
                self.begin = None
            else:  # there is more than 1 node
                self.end = self.end.prev
                self.end.next = None

                if self.end == self.begin:
                    # if there is 1 node left, make begin and end same
                    self.begin.next = None

            self.count -= 1  # keep count of the number of nodes
            return value

        else:
            return None

    def shift(self, obj: str):
        """Appends a new value at the beginning of list."""

        if self.begin is None:  # there is no node in the list
            self.begin = DoubleLinkedListNode(obj, None, None)
            self.end = self.begin
        else:  # there is at least 1 node in the list
            node = DoubleLinkedListNode(obj, self.begin, None)
            self.begin.prev = node
            self.begin = node

        self.count += 1

    def unshift(self) -> None or str:
        """Removes the first item(from begin) and returns it."""
        if self.begin is None:  # if there is no node
            return None
        else:
            removed_value = self.begin.value
            if self.begin == self.end:  # if there is 1 node
                self.begin = None
                self.end = None

            else:  # if there is more than 1 node
                self.begin = self.begin.next
                self.begin.prev = None

            self.count -= 1
            return removed_value

    def detach_node(self, node: DoubleLinkedListNode):
        """You'll need to use this operation sometimes, but mostly
        inside remove(). It should take a node, and detach it from the
        list, whether the node is at the front, end, or in the middle."""
        if node == self.end:
            self.pop()
        elif node == self.begin:
            self.unshift()
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.count -= 1

    def remove(self, obj: str) -> int:
        """Finds a matching item and removes it from the list and returns the index of the removed node."""
        count = 0
        node = self.begin

        while node:
            if node.value == obj:
                self.detach_node(node)
                return count

            node = node.next
            count += 1

        return -1

    def first(self) -> None or str:
        """Returns a *reference* to the first item, does not remove."""
        if self.begin is None:
            return None
        else:
            return self.begin.value

    def last(self) -> None or str:
        """Returns a reference to the last item, does not remove."""
        if self.end is None:
            return None
        else:
            return self.end.value

    def get(self, index: int):
        """Get the value at index."""
        node = self.begin
        count = 0
        while node:
            if count == index:
                return node.value
            node = node.next
            count += 1

    def dump(self, mark: str):
        """Debugging function that dumps the contents of the list."""
        print(mark)
        node = self.begin
        while node:
            print(node, " ", end='')
            node = node.next
        print()
