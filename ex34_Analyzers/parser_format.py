class Parser(object):

    def __init__(self, scanner):
        self.scanner = scanner

    def match(self, token_id):
        return self.scanner.match(token_id)

    def peek(self):
        return self.scanner.peek()

    def skip(self, tokens):
        return self.scanner.skip(tokens)

    def push(self, rule):
        return self.scanner.push(rule)

    def done(self):
        return self.scanner.done()

