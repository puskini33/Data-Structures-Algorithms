"""
Author: Elena Hirjoaba
Date: 10.17.2019
Changes: count() removed
"""


class StackNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class Stack(object):
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, obj):
        """Pushes a new value to the top of the stack."""
        node = StackNode(obj, None)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.count += 1

    def pop(self) -> None or str:
        """Pops the value that is currently on top of the stack."""
        if self.top is None:
            return None
        else:
            popped_node = self.top.value
            self.top = self.top.next
            self.count -= 1
            return popped_node

    def top_node(self) -> None or str:
        """Returns a *reference* to the first item, does not remove."""
        if self.top is None:
            return None
        else:
            return self.top.value

    def dump(self, mark: str = "----") -> str:
        """Debugging function that dumps the contents of the stack."""
        if self.top is None:
            return 'No node in the stack'
        else:
            print(mark)
            node = self.top
            while node:
                print(node, ' ', end='')
                node = node.next
            print()
