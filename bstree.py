class BSTreeNode(object):

    def __init__(self, key, value, left, right, parent):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def find_minimum(self):
        pass

    def replace_node_in_parent(self):
        pass

    def __repr__(self):
        """Function sets how the node is displayed when printed."""
        rkey = self.right and self.right.key or None
        lkey = self.left and self.left.key or None
        pkey = self.parent and self.parent.key or None
        return f'[{self.key}, {self.value}, {repr(lkey)}, {repr(rkey)}, {repr(pkey)}]'


class BSTreeList(object):
    def __init__(self):
        self.root = None
        self.count = 0

    """def push(self, key, value):
        # push is similar to get
        node = BSTreeNode()
        if self.root is None:  # there is 1 node
            node = BSTreeNode(None, None, key, value, None)
            self.root = node
        elif: # there are 2 nodes?
            pass
        else:
            if self.root.left is None:
                self.root.left = node
                # node.prev =
            elif self.root.right is None:
                self.root.right = node"""

    def _get(self, key, node):
        """Use this function for recursion"""
        pass

    def get(self, key: int) -> BSTreeNode or None:
        """Given a key, the function returns the found node or None."""
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
        """If unexistent, function attaches a new node to the tree."""
        if self.root is None:  # there is no node in the tree
            self.root = BSTreeNode(key, value, None, None, None)
            self.count += 1
            return self.count
        elif self.root:  # there is at least 1 node in the tree
            found = self.get(key)
            if found is None:  # if the node has not been found in the tree
                child = self.root
                while child:
                    if key >= child.key:
                        if child.right is None:  # if the node has no right child, create
                            BSTreeNode(key, value, None, None, child)
                            self.count += 1
                            return self.count
                        child = child.right
                    elif key < child.key:
                        if child.left is None:  # if the node has no left child, create
                            child.left = BSTreeNode(key, value, None, None, child)
                            self.count += 1
                            return self.count
                        child = child.left
            else:
                return ' Node is already in the tree.'

    def delete(self):
        # Condition 1: the node is leaf(no children)
        # remove the leaf

        # Condition 2: the node has 1 child
        # replace the root with the child
        # Condition 3: the node has 2 children
        # find the minimum child of the D.right node (called successor)
        # set the D.key to successor.key
        # repeat to successor's children using its key
        pass

    def list(self):
        # traverse tree
        # print the nodes (there is more than 1 way to do it)
        pass


letters = BSTreeList()
letters.set(9, 'Z')
letters.set(6, 'A')
letters.set(3, 'G')
letters.set(4, 'F')
assert letters.set(1, 'L') == 5
