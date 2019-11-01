class SuffixArray(object):

    def __init__(self, instr):
        self.instr = instr  # string to be searched in
        sfx = []
        for i in range(0, len(instr)):
            sfx.append((self.instr[i:], i))  # tuple of substring, index of substring
        # sfx is now a list of tuples containing (substring, index)
        self.sarray = sorted(sfx)  # the sorted list

    def search(self, what: str):
        """
        Uses a binary search to find two indexes:
        first is where it is in self.sarray - list of substrings
        second is where it is in self.instr - string
        """

        low = 0
        high = len(self.sarray)  # number of substrings

        while low < high:
            mid = (high - low) // 2 + low  # calculate the mid index
            mid_val, starts_at = self.sarray[mid]  # tuple (substring, index) at mid index

            if mid_val == what:  # if substrings match
                return mid, starts_at  # return index at middle, and index of substring
            elif mid_val > what:
                high = mid  # select the left side of the list
            elif mid_val < what:
                low = mid + 1  # select the right side of the list

        return -1, -1  # if the substring is not found, return -1, -1

    def find_shortest(self, match):
        """Easiest is assume exact match of suffix."""
        sarray_i, instr_i = self.search(match)  # index at middle and index of matched substring is returned
        return instr_i  # returns the index of the match from inside the tuple

    def find_longest(self, match):
        sarray_i, instr_i = self.search(match)  # index at middle and index of matched substring is returned
        if sarray_i == -1:
            return -1, -1  # if the index is not found, return -1, -1

        test, instr_i = self.sarray[sarray_i]  # substring, index in tupple
        longest, longest_i = test, instr_i

        while test.startswith(match):  # checks if string starts with; returns True or False
            if len(test) > len(longest):
                longest, longest_i = test, instr_i  # update the longest string

            sarray_i += 1  # increase the index in the list to find the next tuple

            try:
                test, instr_i = self.sarray[sarray_i]
            except IndexError:  # if the list is out of index
                break

        return longest, longest_i

    def find_all(self, match):
        sarray_i, instr_i = self.search(match)  # index of tuple in list, and index of substring in string
        if sarray_i == -1:  # if not found
            return -1, -1

        test, instr_i = self.sarray[sarray_i]  # substring and the index of substring in string
        results = []

        while test.startswith(match):  # while test starts with the match, substring
            results.append((test, instr_i))  # append the result
            sarray_i += 1  # increase index, and search for more

            try:
                test, instr_i = self.sarray[sarray_i]
            except IndexError:
                break

        return results
