class SingleLinkedListNode(object):

    def __init__(self, value: None or int, nxt: 'SingleLinkedListNode' or None = None):
        self.value = value
        self.next = nxt

    def __repr__(self):
        """The repr() method returns a printable representational string of the given object."""
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


def manually_print_single_linked_list():
    list_of_nodes = []
    head = SingleLinkedListNode(None, None)
    list_of_nodes.append(head)
    print(list_of_nodes)
    node1 = SingleLinkedListNode(10)
    head = SingleLinkedListNode(None, node1)
    list_of_nodes[-1] = head
    list_of_nodes.append(node1)
    print(list_of_nodes)
    node2 = SingleLinkedListNode(20, None)
    node1 = SingleLinkedListNode(10, node2)
    list_of_nodes[-1] = node1
    list_of_nodes.append(node2)
    print(list_of_nodes)


class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None
        self.count = 0

    def push(self, obj: str):
        """Appends a new value at the end of the list."""
        node = SingleLinkedListNode(obj)
        if self.begin is None:  # no node in the list
            self.begin = node
            self.end = self.begin
        else:  # there is more than 1 node in the list
            self.end.next = node
            self.end = node

        self.count = self.count + 1

    def pop(self) -> str or None:
        """Removes the last item and returns the value of it."""
        if self.begin is None:
            assert self.end is None
            return None
        elif self.begin == self.end:
            value = self.begin.value
            self.begin = None
            self.end = None
            self.count = self.count - 1
            return value

        current = self.begin
        print(self.end)
        while current.next != self.end:
            current = current.next

        value = self.end.value
        self.end = current
        self.end.next = None
        self.count = self.count - 1
        return value

    def shift(self, obj):
        """Pushes at the beginning of the list."""
        node = SingleLinkedListNode(obj, None)
        if self.begin is None:
            self.begin = node
        elif self.begin.next is None:
            self.end = self.begin
            self.begin = node
            self.begin.next = self.end
        else:
            node.next = self.begin
            self.begin = node

        self.count = self.count + 1

    def unshift(self):
        """Removes the first item and returns it."""
        if self.begin is None:
            return None
        else:
            removed_node = self.begin.value
            self.begin = self.begin.next
            self.count = self.count - 1
            return removed_node

    def remove(self, obj: str):
        """Finds a matching item and removes it from the list."""

        if self.begin is None:
            return None
        else:  # at least one node exists
            node = self.begin
            number_reference_node = 0
            if self.begin.value == obj:  # searched item is in the first node
                number_reference_node = 0
                self.begin = self.begin.next
                self.count = self.count - 1
                return number_reference_node

            while node.next:  # searched item is in the second or in the following nodes
                node_before_node = node
                node = node.next
                if node.next is not None:
                    node_after_node = node.next

                if node.value == obj and node.next is not None:  # if searched node is in the list
                    node_before_node.next = node_after_node
                    number_reference_node += 1
                    self.count = self.count - 1
                    return number_reference_node
                elif node.value == obj and node.next is None:  # if searched node is at the end of list
                    node_before_node.next = None
                    number_reference_node += 1
                    self.count = self.count - 1
                    return number_reference_node

                number_reference_node += 1
            return number_reference_node

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

    def get(self, index):
        """Get the value at index."""
        node = self.begin
        index_value = 0
        while node:
            if index_value == index:
                return node.value
            node = node.next
            index_value += 1

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        return
