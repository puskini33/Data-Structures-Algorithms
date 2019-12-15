from runner import Runner
from Scanner import Scanner
from parser_format import Parser
import unittest
from pprint import pprint


class TestRunner(unittest.TestCase):

    def test_main(self):
        first_scanner = Scanner(TOKENS, code)
        print('List of tokens after lexical analysis contains: ')
        pprint(first_scanner.list_tokens)
        first_parser = Parser(first_scanner)
        trial = Runner(first_parser)
        main = trial.main()
        return main


code = ["def hello(x, y):", "    pprint(x + y)", "hello(10, 20)"]

TOKENS = [
        ((r"^def"),                    "DEF"),
        ((r"^[a-zA-Z_][a-zA-Z0-9_]*"), "NAME"),
        ((r"^[0-9]+"),                 "INTEGER"),
        ((r"^\("),                     "LPAREN"),
        ((r"^\)"),                     "RPAREN"),
        ((r"^\+"),                     "PLUS"),
        ((r"^:"),                      "COLON"),
        ((r"^,"),                      "COMMA"),
        ((r"((\s\s\s\s)|\t)"),         "INDENT"),
        ((r"\s"),                      "SPACE")]

if __name__ == '__main__':
    unittest.main(verbosity=2)
