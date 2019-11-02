"""This code uses the binary tree to sort and search for substrings."""


class BSTreeNode(object):

    def __init__(self, key, value, left, right, parent):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self) -> str:
        """Function sets how the node is displayed when printed."""
        rkey = self.right and self.right.key or None
        lkey = self.left and self.left.key or None
        pkey = self.parent and self.parent.key or None
        return f'[{self.key}, {self.value}, {repr(lkey)}, {repr(rkey)}, {repr(pkey)}]'


class SuffixArray(object):

    def __init__(self, full_string):
        self.root = None
        self.full_string = full_string
        for i in range(0, len(full_string)):
            self.set(full_string[i:], i)

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

    def find_shortest(self, match: str) -> int:
        """Function returns the index of shortest found substring."""
        key_substring = self.get(match)
        if key_substring is None:
            return -1

        return key_substring.value

    def find_longest(self, match: str) -> int:
        """Function searches and returns the longest substring."""
        key_match = self.get(match)
        if key_match is None:
            return -1

        value_substring, instr_index = key_match.key, key_match.value
        longest_string, index_longest = value_substring, instr_index

        while value_substring.startswith(match):
            if len(value_substring) > len(longest_string):
                longest_string, index_longest = value_substring, instr_index  # update longest

            key_match = key_match.parent

            value_substring, instr_index = key_match.key, key_match.value

        return index_longest

    def find_all(self, match: str) -> list:
        """Function searches and returns the list of all substrings that start with match"""
        key_match = self.get(match)

        if key_match is None:
            return -1, -1

        value_substring, instr_index = key_match.key, key_match.value
        suffix_array_list = []

        while value_substring.startswith(match):
            suffix_array_list.append((value_substring, instr_index))  # append found substring

            key_match = key_match.parent

            value_substring, instr_index = key_match.key, key_match.value

        return suffix_array_list
