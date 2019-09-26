from DLL_Code import DoubleLinkedList


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
        self.double_ll = DoubleLinkedList()

    def shift(self, obj: str):
        """Appends the node at the tail of the queue."""
        self.double_ll.push(obj)

    def unshift(self):
        """Removes the node from the head of the queue and returns the value of the returned node."""
        self.double_ll.unshift()