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
        self.before_last = None

    def push(self, obj: str):
        """Appends a new value at the end of the list."""
        node = SingleLinkedListNode(obj, None)
        if self.begin is None:
            self.begin = node
            assert self.begin is not None
        elif self.begin.next is None:
            self.end = node
            self.begin.next = self.end
        else:
            self.before_last = self.end
            self.end = node
            self.before_last.next = self.end

    def pop(self) -> str or None:
        """Removes the last item and returns it."""
        last_node = self.begin
        removed_node = None
        if last_node is None:
            return None
        elif last_node.next is None:  # pop begin
            removed_node = self.begin
            self.begin = None
        else:
            while last_node.next.next:
                last_node = last_node.next
            removed_node = last_node.next
            last_node.next = None
        return removed_node.value

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
        # This function takes a lot of time and if every time done
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


