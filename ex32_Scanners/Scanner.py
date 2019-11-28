import re

class Scanner(object):

    def __init__(self, regex_rules: 'list of tuples', text_to_match: list):
        self.rules = regex_rules
        self.text_to_match = text_to_match
        self.list_tokens = []  # list of tuples
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

    def try_match(self, i: int, line: str):
        """Given a list of possible tokens, returns the first one that matches the first token in the list
        and removes it."""
        start = line[i:]  # take the unmatched string
        for regex, token in self.rules:  # for each set regex and token (tuple)
            compiled_regex = re.compile(regex)
            match = compiled_regex.match(start)  # verify to see if the string matches the regex
            if match:  # if a match is found
                begin, end = match.span()  # take the begin and end index
                """ Span returns a tuple containing the (start, end) positions of the match"""
                return token, start[:end], end  # return TOKEN
        return None, start, None

    def match(self, token_id):
        """Given a list of possible tokens, returns the first one that matches the first token in the list
    and removes it."""

        if self.list_tokens[0][0] == token_id[0]:
            removed = self.list_tokens.pop(0)
            return [removed[0], removed[1]]
        else:
            return ['ERROR', 'error']

    def peek(self, token_id):
        """Given a list of possible tokens, returns which ones could work with match but does not
        remove it from the list."""
        if self.list_tokens[0][0] == token_id[0]:
            return [self.list_tokens[0][0], self.list_tokens[0][1]]
        else:
            return ['ERROR', 'error']

    def skip(self, *what):
        """Function evaluates if first element in the given list of tokens equals the first element
        in the list of tokens of the object. If YES, it returns TRUE, if NOT, it pops the first element and
        tries again, and returns False if also first new element does not match."""
        for x in what:
            if x != self.list_tokens[0]:
                self.list_tokens.pop(0)

            tok = self.list_tokens[0]
            if tok[0] != x:
                return False
            else:
                self.list_tokens.pop(0)

        return True

    def push(self, rule_token):
        """Pushes a token back on the token stream so that a later peek or match will return it."""
        for i in range(0, len(self.list_tokens)):
            if rule_token[1] == self.list_tokens[i][0]:
                continue
            else:
                self.rules.append(rule_token)

    def done(self):
        return len(self.list_tokens) == 0


code = [
"def hello(x, y):",
"    print(x + y)",
"hello(10, 20)",
]

TOKENS = [
        (re.compile(r"^def"),                    "DEF"),
        (re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*"), "NAME"),
        (re.compile(r"^[0-9]+"),                 "INTEGER"),
        (re.compile(r"^\("),                     "LPAREN"),
        (re.compile(r"^\)"),                     "RPAREN"),
        (re.compile(r"^\+"),                     "PLUS"),
        (re.compile(r"^:"),                      "COLON"),
        (re.compile(r"^,"),                      "COMMA"),
        (re.compile(r"^\s+"),                    "INDENT")
]

token_id = ["DEF", "NAME", "INTEGER", "LPAREN", "RPAREN", "PLUS", "COLON", "COMMA", "INDENT"]


first_scanner = Scanner(TOKENS, code)
first_scanner.match(token_id)
first_scanner.skip(token_id)
first_scanner.peek(token_id)
