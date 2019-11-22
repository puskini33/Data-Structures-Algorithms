class Scanner(object):

    def __init__(self, regex_rules: 'list of tuples', text_to_match: list):
        self.rules = regex_rules
        self.text_to_match = text_to_match
        self.list_tokens = []
        self.scan()

    def scan(self):
        """Takes a string and runs the scan on it, creating a list of tokens for later. You should keep
        this string around for people to access later."""
        for line in self.text_to_match:  # taking each line from the code to match
            i = 0
            while i < len(line):  # looping till the end of the string is reached
                token, string, end = self.try_match(i, line)  # i = 3, line = code[0]
                assert token, 'Failed to match line %s' % string

                if token:  # if a token is matched
                    i += end  # set the new index to take the unmatched string
                    self.list_tokens.append((token, string, i, end))  # append the found goods
        print(self.list_tokens)

    def try_match(self, i: int, line: str):
        start = line[i:]  # take the unmatched string
        for regex, token in self.rules:  # for each set regex and token (tuple)
            compiled_regex = re.compile(regex)
            match = compiled_regex.match(start)  # verify to see if the string matches the regex
            if match:  # if a match is found
                begin, end = match.span()  # take the begin and end index
                """ Span returns a tuple containing the (start, end) positions of the match"""
                return token, start[:end], end  # return TOKEN
        return None, start, None


    def ignore_ws(self):
        while self.list_tokens[0][0] == 'INDENT':
            self.list_tokens.pop(0)

    def match(self, token_id):
        """Given a list of possible tokens, returns the first one that matches the first token in the list
    and removes it."""
        if token_id != 'INDENT':
            self.ignore_ws()

        if self.list_tokens[0][0] == token_id:
            return self.tokens.pop(0)
        else:
            return ['ERROR', 'error']

    def peek(self):
        """Given a list of possible tokens, returns which ones could work with match but does not
        remove it from the list."""
        self.ignore_ws()
        return self.list_tokens[0][0]

    def skip(self, *what):
        for x in what:
            if x != 'INDENT': self.ignore_ws()

            tok = self.tokens[0]
            if tok[0] != x:
                return False
            else:
                self.tokens.pop(0)

        return True

    def push(self):
        """Pushes a token back on the token stream so that a later peek or match will return it."""
