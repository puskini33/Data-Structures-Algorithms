from Scanner import Scanner
import unittest


class ScannerTest(unittest.TestCase):

    def test_scanner(self):
        local_scanner = Scanner(tokens, code)
        self.assertIsNotNone(local_scanner.list_tokens)
        local_scanner.skip('DEF')
        self.assertEqual(local_scanner.list_tokens[0][0], 'SPACE')
        local_scanner.skip('SPACE')
        local_scanner.match('NAME')
        self.assertNotEqual(local_scanner.list_tokens[0][0], 'NAME')

        del tokens[:]
        another_local_scanner = Scanner(tokens, code)
        self.assertEqual(another_local_scanner.scan(), 'Failed to match line def publish(x, y):')
        self.assertEqual(another_local_scanner.list_tokens, [])


code = ["def publish(x, y):", "    print(x + y)", "publish(10, 20)"]

tokens = [
        ((r"^def"),                    "DEF"),
        ((r"^[a-zA-Z_][a-zA-Z0-9_]*"), "NAME"),
        ((r"^[0-9]+"),                 "INTEGER"),
        ((r"^\("),                     "LPAREN"),
        ((r"^\)"),                     "RPAREN"),
        ((r"^\+"),                     "PLUS"),
        ((r"^:"),                      "COLON"),
        ((r"^,"),                      "COMMA"),
        ((r"((\s\s\s\s)|\t)"),         "INDENT"),
        ((r"\s"),                      "SPACE")
]


if __name__ == '__main__':
    trial = ScannerTest()
    trial.test_scanner()
    unittest.main(verbosity=2)
