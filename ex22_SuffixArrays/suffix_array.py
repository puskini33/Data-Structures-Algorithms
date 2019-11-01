class SuffixArray(object):

    def __init__(self, full_string):
        self.full_string = full_string
        list_tuples_substrings = []
        for i in range(0, len(full_string)):
            list_tuples_substrings.append((full_string[i:], i))
        self.suffix_array = sorted(list_tuples_substrings)

    def search(self, match: str) -> tuple:
        """Function uses binary search to search for a substring in a list of tuples (substrings, index) of a string"""
        low = 0
        high = len(self.suffix_array)

        while low < high:
            middle_index = (high - low) // 2 + low  # why exactly this formula?
            middle_value, instring_index = self.suffix_array[middle_index]

            if match == middle_value:
                return middle_index, instring_index
            elif match < middle_value:
                high = middle_index
            elif match > middle_value:
                low = middle_index + 1

        return -1, -1

    def find_shortest(self, match: str) -> int:
        """Function returns the shortest found substring."""
        middle_index, instr_index = self.search(match)
        return instr_index

    def find_longest(self, match: str) -> tuple:
        """Function searches and returns the longest substring."""
        middle_index, instr_index = self.search(match)

        if middle_index == -1:
            return -1, -1

        value_substring, instr_index = self.suffix_array[middle_index]
        longest_string, index_longest = value_substring, instr_index

        while value_substring.startswith(match):
            if len(value_substring) > len(longest_string):
                longest_string, index_longest = value_substring, instr_index  # update longest

            middle_index += 1

            try:
                value_substring, instr_index = self.suffix_array[middle_index]  # get value for next substring
            except IndexError:
                break

        return longest_string, index_longest

    def find_all(self, match: str) -> list:
        """Function searches and returns the list of all substrings that start with match"""
        middle_index, instr_index = self.search(match)

        if middle_index == -1:
            return -1, -1

        value_substring, instr_index = self.suffix_array[middle_index]
        suffix_array_list = []

        while value_substring.startswith(match):
            suffix_array_list.append((value_substring, instr_index))  # append found substring

            middle_index += 1

            try:
                value_substring, instr_index = self.suffix_array[middle_index]  # get the next substring
            except IndexError:
                break

        return suffix_array_list
