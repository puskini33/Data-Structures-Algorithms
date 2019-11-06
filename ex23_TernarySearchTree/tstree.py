class TSTreeNode(object):

    def __init__(self, char, key, value, low, high, eq):
        self.key = key
        self.value = value
        self.low = low
        self.high = high
        self.eq = eq
        self.char = char

    def __repr__(self):
        return f"{self.char}, {self.key}:{self.value}<{self.low and self.low.key}={self.eq and self.eq.key}={self.high and self.high.key}>"



class TSTree(object):

    def __init__(self):
        self.root = None

    def _set(self, chars, key, value, node):
        char = chars[0]

        if not node:
            node = TSTreeNode(char, None, None, None, None, None)  # why isn'T value passed here?

        if char < node.char:
            node.low = self._set(chars, key, value, node.low)
        elif node.char == char:
            if len(chars) > 1:
                node.eq = self._set(chars[1:], key, value, node.eq)
            else:
                node.value = value
                node.key = key
        elif char > node.char:
            node.high = self._set(chars, key, value, node.high)

        return node

    def set(self, key, value):
        chars = [ord(x) for x in key]
        self.root = self._set(chars, key, value, self.root)

    def _get(self, chars, node):
        char = chars[0]

        if not node:
            return None
        elif char < node.char:
            return self._get(chars, node.low)
        elif node.char == char:
            if len(chars) > 1:
                return self._get(chars[1:], node.eq)
            else:
                return node
        elif char > node.char:
            return self._get(chars, node.high)

    def get(self, key):
        chars = [ord(x) for x in key]
        node = self._get(chars, self.root)
        return node and node.value or None

    def find_shortest(self, key):
        list_strings = self.find_all(key)
        if not list_strings:
            return None

        shortest = list_strings[0]

        for node in list_strings:
            if len(node.key) < len(shortest.key):
                shortest = node

        return shortest

    def find_longest(self, key):
        list_strings = self.find_all(key)
        if not list_strings:
            return None

        longest = list_strings[0]

        for node in list_strings:
            if len(node.key) > len(longest.key):
                longest = node

        return longest

    def _find_all(self, node, list_strings, key):
        if not node:
            return

        if node.key and node.value:
            list_strings.append(node)

        if node.low:
            self._find_all(node.low, list_strings, key)

        if node.eq:
            self._find_all(node.eq, list_strings, key)

        if node.high:
            self._find_all(node.high, list_strings, key)

    def find_all(self, key):
        all_strings = []
        chars = [ord(x) for x in key]
        start = self._get(chars, self.root)
        if start:
            self._find_all(start.eq, all_strings, key)
        return all_strings

    def find_part(self, key):
        found = self.find_shortest(key[:1])

        if not found:
            return None

        for i in range(2, len(key)):
            stem = key[:i]
            node = self.find_shortest(stem)
            if node:
                found = node
            else:
                return found

        return found
