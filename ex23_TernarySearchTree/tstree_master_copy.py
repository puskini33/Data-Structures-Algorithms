class TSTreeNode(object):

    def __init__(self, char, key, value, low, eq, high):
        self.char = char
        self.key = key
        self.low = low
        self.eq = eq
        self.high = high
        self.value = value

    def __repr__(self):
        return f"{self.char}, {self.key}:{self.value}<{self.low and self.low.key}={self.eq and self.eq.key}={self.high and self.high.key}>"


class TSTree(object):

    def __init__(self):
        self.root = None

    def _get(self, node, chars) -> TSTreeNode or None:
        """Given root and the list of char, function returns the found node or None"""
        char = chars[0]  # take the first char
        if not node:
            return None
        elif char < node.char:  # if smaller, go low
            return self._get(node.low, chars)
        elif char == node.char:  # if equal and length of list > 1, go equal
            if len(chars) > 1:
                return self._get(node.eq, chars[1:])
            else:  # if length < 1, return the found node
                return node
        else:  # if bigger, go higher
            return self._get(node.high, chars)

    def get(self, key: str) -> int or None:
        chars = [ord(x) for x in key]  # letters in the string are transformed into numbers
        node = self._get(self.root, chars)  # get the last node that matches the last element in chars
        return node and node.value or None

    def _set(self, node, chars, key, value) -> TSTreeNode:
        """Function returns the first node that was initialized."""
        next_char = chars[0]  # take the first number in the chars list

        if not node:  # if not node, create one
            # what happens if you add the value here?
            node = TSTreeNode(next_char, None, None, None, None, None)

        if next_char < node.char:  # if smaller, go low
            node.low = self._set(node.low, chars, key, value)
        elif next_char == node.char:  # if equal and length of list > 1, go middle
            if len(chars) > 1:
                node.eq = self._set(node.eq, chars[1:], key, value)
            else:  # if length < 1, set the value and key of the last node
                # what happens if you DO NOT add the value here?
                node.value = value
                node.key = key
        else:  # if bigger, go high
            node.high = self._set(node.high, chars, key, value)

        return node  # return the first node that was created

    def set(self, key: str, value: int):
        """Function sets the root of the ternary tree."""
        chars = [ord(x) for x in key]  # letters in the string are transformed into numbers
        self.root = self._set(self.root, chars, key, value)  # set the self.root

    def find_shortest(self, key: str) -> TSTreeNode or None:
        nodes = self.find_all(key)  # get list of all nodes
        if nodes:
            shortest = nodes[0]  # the shortest is the first node in the list
            for node in nodes:
                if len(node.key) < len(shortest.key):  # if there is a shorter element in the list assign it to shortest
                    shortest = node
            return shortest
        else:
            return None

    def find_longest(self, key: str) -> TSTreeNode:
        nodes = self.find_all(key)  # get list of all nodes
        longest = nodes[0]  # longest is first element in the list
        for node in nodes:
            if len(node.key) > len(longest.key):  # if there is a longer element, that is the longest
                longest = node
        return longest

    def _find_all(self, node: TSTreeNode, key, results):
        if not node:
            return

        if node.key and node.value:  # if current node has key and value, append
            # this node has something so save it
            results.append(node)

        # if there is a low then go low
        if node.low:
            self._find_all(node.low, key, results)

        if node.eq:
            # now follow middle
            self._find_all(node.eq, key, results)

        if node.high:
            # if there is a high then go high
            self._find_all(node.high, key, results)

    def find_all(self, key: str) -> list:
        results = []
        chars = [ord(x) for x in key]  # transform the letters into numbers
        start = self._get(self.root, chars)  # get the last node that matches the last element in chars
        if start:
            self._find_all(start.eq, key, results)  # find all nodes that are derived from start
        return results

    def find_part(self, key: str) -> TSTreeNode or None:
        """The difference between part and shortest is this:
        If you give find_part a 10 char key, and only 2 chars of the key
        match 2 chars in the TSTree, then it will return that key. It is
        partial on *both* search key and key/value key.

        If you give a 10 char key to shortest, and only 2 chars match then
        it doesn't find anything.
        """
        # start by just finding the shortest key starting with the first char
        found = self.find_shortest(key[:1])  # get the shortest
        if not found:
            return None

        # now if we found something then keep increasing the key
        for i in range(2, len(key)):
            stem = key[:i]
            node = self.find_shortest(stem)
            if not node:
                # didn't find something with the new key, so return what we've found so far
                return found
            else:
                # found something, so update the best match so far
                found = node

        return found


full_string = TSTree()
full_string.set('apple', 6)
full_string.set('application', 11)

full_string.get('appl')
full_string.find_all('appl')
full_string.find_part('applom')
