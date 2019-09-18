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
        # node = SingleLinkedListNode(obj, None)
        if self.begin is None:
            self.begin = SingleLinkedListNode(obj, None)
            self.end = self.begin
        elif self.end == self.begin:
            self.end = SingleLinkedListNode(obj, None)
            self.begin.next = self.end

        else:
            node = self.end
            self.end = SingleLinkedListNode(obj, None)
            node.next = self.end

    def count(self):
        """Counts the number of elements in the list."""
        node = self.begin
        count = 0
        while node:
            count += 1
            node = node.next
        print(count)
        return count


colors = SingleLinkedList()
colors.push('Green')
colors.push('Red')
colors.count()


