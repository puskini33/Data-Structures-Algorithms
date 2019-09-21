def pop(self, input) -> str or None:
    """Removes the last item and returns it."""
    node = self.begin
    popped_node = None
    if node is None:
        return None
    elif node.next is None:
        removed_value = self.begin.value
        self.begin = None
        node = self.begin
    else:
        node = self.begin
        while node.next.next:
            node = node.next

    return removed_value

pop('Alireza')
