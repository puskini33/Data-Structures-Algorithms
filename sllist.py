class SingleLinkedListNode(object):

    def __init__(self, value: None or int, nxt: 'object' or int = None) -> str:
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
        self.before_last = None

    def push(self, obj: str) -> str:
        """Appends a new value at the end of the list."""
        # TODO: improve this code
        node = SingleLinkedListNode(obj, None)
        if self.begin is None:
            self.begin = node
        elif self.begin.next is None:
            self.end = node
            self.begin.next = self.end
        else:
            self.before_last = self.end
            self.end = node
            self.before_last.next = self.end

    def pop(self):
        """Removes the last item and returns it."""
        # TODO: continue coding here
        while self.begin:
            current_node = self.begin.next

        self.before_last.next = None
        # remove last item self.end and return the value of the removed object
        if self.end.next is None:
            value = self.end.value
            self.end = self.before_last
            return value
        # the before last item is the new last item
        # I have to count again the items
        else:
            pass


        # the new last item should be of the format (obj, None)

    def shift(self, obj):
        """Another name for push."""

    def unshift(self):
        """Removes the first item and returns it."""

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""

    def first(self):
        """Returns a *reference* to the first item, does not remove."""

    def last(self):
        """Returns a reference to the last item, does not remove."""

    def count(self):
        """Counts the number of elements in the list."""
        node = self.begin
        count = 0
        while node:
            count += 1
            node = node.next

        return count

    def get(self, index):
        """Get the value at index."""

    def dump(self):
        """Debugging function that dumps the contents of the list."""
