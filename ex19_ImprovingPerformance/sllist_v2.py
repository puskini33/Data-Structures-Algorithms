class SingleLinkedListNode(object):

    def __init__(self, value: None or int, nxt: 'object' or int = None):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"
        # The repr() method returns a printable representational string of the given object.


def manually_print_single_linked_list():
    list_of_nodes = []
    head = SingleLinkedListNode(None, None)
    list_of_nodes.append(head)
    print(list_of_nodes)
    node1 = SingleLinkedListNode(10, None)
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
        node = SingleLinkedListNode(obj, None)
        if self.begin is None:  # no node in the list
            self.begin = node
            self.end = self.begin
        elif self.begin.next is None:  # there is only one node in the list
            self.end = node
            self.begin.next = self.end
        else:  # there are more than 1 node in the list
            self.end.next = node
            self.end = node

        self.add_to_count()

    def pop(self) -> str or None:
        """Removes the last item and returns it."""
        last_node = self.begin
        removed_node = None
        if last_node is None:
            return None
        elif last_node.next is None:
            removed_node = self.begin
            self.begin = None
        else:
            while last_node.next.next:
                last_node = last_node.next
            removed_node = last_node.next
            last_node.next = None

        self.remove_from_count()
        return removed_node.value

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

        self.add_to_count()

    def unshift(self):
        """Removes the first item and returns it."""
        if self.begin is None:
            return None
        else:
            removed_node = self.begin.value
            self.begin = self.begin.next
            self.remove_from_count()
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
                self.remove_from_count()
                return number_reference_node

            while node.next:  # searched item is in the second or in the following nodes
                node_before_node = node
                node = node.next
                if node.next is not None:
                    node_after_node = node.next

                if node.value == obj and node.next is not None:  # if searched node is in the list
                    node_before_node.next = node_after_node
                    number_reference_node += 1
                    self.remove_from_count()
                    return number_reference_node
                elif node.value == obj and node.next is None:  # if searched node is at the end of list
                    node_before_node.next = None
                    number_reference_node += 1
                    self.remove_from_count()
                    return number_reference_node

                number_reference_node += 1
                self.remove_from_count()
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

    def add_to_count(self):
        """ Adds to the number of elements in the list."""
        self.count = self.count + 1
        return self.count

    def remove_from_count(self):
        if self.count == 0:
            print('Number of nodes is 0, you cannot substract.')
            exit(1)

        self.count = self.count - 1
        return self.count

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


