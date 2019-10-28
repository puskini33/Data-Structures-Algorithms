class BSTreeNode(object):

    def __init__(self, key, value, left, right, parent):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def find_minimum(self) -> 'BSTreeNode':
        """Finds the smallest value of the right side of the node (i.e., node.right)."""
        node = self
        while node.left:
            node = node.left
        return node

    def replace_node_in_parent(self, child: 'BSTreeNode'):
        if self.parent:
            print(self.parent)
            if self == self.parent.left:
                self.parent.left = child
            else:
                self.parent.right = child

        if child:
            child.parent = self.parent

    def __repr__(self) -> str:
        """Function sets how the node is displayed when printed."""
        rkey = self.right and self.right.key or None
        lkey = self.left and self.left.key or None
        pkey = self.parent and self.parent.key or None
        return f'[{self.key}, {self.value}, {repr(lkey)}, {repr(rkey)}, {repr(pkey)}]'


class BSTreeList(object):
    def __init__(self):
        self.root = None

    def get(self, key: int) -> BSTreeNode or None:
        """Given a key, the function returns the found node or None.."""
        if self.root is None:
            return None

        node = self.root
        while node:
            if key == node.key:
                return node
            elif node.right is None and node.left is None:
                return None
            elif key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right

    def set(self, key: int, value: int or str):
        """If nonexistent, function attaches a new node to the tree."""
        if self.root is None:  # there is no node in the tree
            self.root = BSTreeNode(key, value, None, None, None)
        elif self.root:  # there is at least 1 node in the tree
            found = self.get(key)
            if found is None:  # if the node has not been found in the tree
                child = self.root
                while child:
                    if key >= child.key:
                        if child.right is None:  # if the node has no right child, create
                            child.right = BSTreeNode(key, value, None, None, child)
                            break
                        child = child.right
                    elif key < child.key:
                        if child.left is None:  # if the node has no left child, create
                            child.left = BSTreeNode(key, value, None, None, child)
                            break
                        child = child.left
            elif found:
                found.value = value

    def _delete(self, key: str or int, node: 'BSTreeNode'):
        """Deletes found node in the tree."""
        assert node, """Invalid node given"""
        if key < node.key:  # if key is smaller than node.key, go left
            self._delete(key, node.left)
        elif key > node.key:  # if key is bigger than node.key, go right
            self._delete(key, node.right)
        elif key == node.key:
            if node.left and node.right:  # if node has 2 children
                successor = node.find_minimum()
                node.key = successor.key
                self._delete(successor.key, successor)
            elif node.left:  # if node has the left child
                if node is self.root:
                    self.root = node.left
                    node.left.parent = None
                else:
                    node.parent.replace_node_in_parent(node.left)
            elif node.right:  # if node has the right child
                if node is self.root:
                    self.root = node.right
                    node.right.parent = None
                else:
                    node.parent.replace_node_in_parent(node.right)
            elif node.left is None and node.right is None:  # if the node has no children
                if node is self.root:
                    self.root = None
                else:
                    node.parent.left = None
                    node.parent.right = None

    def delete(self, key: str or int) -> None:
        """Using recursion, calls the _delete() function."""
        if self.root:
            self._delete(key, self.root)
        else:
            return None

    def _list(self, node, indent=0):
        """List the elements in the tree."""
        assert node, """Invalid node given"""
        if node:
            print(" " * indent, node.key, "=", node.value)
            if node.left:
                print(" " * indent, "<", end="")
                self._list(node.left, indent+1)

            if node.right:
                print(" " * indent, ">", end="")
                self._list(node.right, indent+1)

    def list(self, start=""):
        print("\n\n----", start)
        self._list(self.root)
