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

    def _invariant(self):
        if self.begin is None:
            assert self.end is None
        elif self.begin.next is None:
            assert self.begin == self.end
        elif self.begin.next is not None:
            assert self.begin.prev is None
            assert self.end.next is None

    def push(self, obj: str):
        """Appends a new value on the end of the list."""
        node = DoubleLinkedListNode(obj, None, None)
        if self.begin is None:
            self.begin = node
            self.end = self.begin
        elif self.end == self.begin:
            self.end = node
            self.begin.next = self.end
            self.end.prev = self.begin
            self._invariant()
        else:
            node.prev = self.end
            self.end.next = node
            self.end = node

    def pop(self) -> str or None:
        """Removes the last item and returns it."""
        if self.begin is None:
            return None
        elif self.end == self.begin:
            returned_value = self.end.value
            self.end = None
            self.begin = None
            return returned_value
        else:
            returned_value = self.end.value
            self.end = self.end.prev
            self.end.next = None
            return returned_value

    def shift(self, obj):
        """Appends a new value at the beginning of list."""
        node = DoubleLinkedListNode(obj, None, None)
        if self.begin is None:
            self.begin = node
            self.end = self.begin
        elif self.begin == self.end:
            self.begin.prev = node
            node.next = self.begin
            self.end = self.begin
            self.begin = node
        else:
            self.begin.prev = node
            node.next = self.begin
            self.begin = node

    def unshift(self) -> None or str:
        """Removes the first item(from begin) and returns it."""
        if self.begin is None:
            return None
        elif self.begin == self.end:
            removed_value = self.begin.value
            self.begin = None
            self.end = None
            return removed_value
        else:
            removed_value = self.begin.value
            self.begin = self.begin.next
            self.begin.prev = None
            return removed_value

    def detach_node(self, node):
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

    def remove(self, obj):
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

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        if self.begin is None:
            return None
        else:
            return self.begin.value

    def last(self):
        """Returns a reference to the last item, does not remove."""
        if self.end is None:
            return None
        else:
            return self.end.value

    def count(self):
        """Counts the number of elements in the list."""
        node = self.begin
        count = 0
        while node:
            node = node.next
            count += 1

        return count

    def get(self, index):
        """Get the value at index."""
        node = self.begin
        count = 0
        while node:
            if count == index:
                return node.value
            node = node.next
            count += 1

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        print(mark)
        node = self.begin
        while node:
            print(node, " ", end='')
            node = node.next
        print()
