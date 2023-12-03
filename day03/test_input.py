import unittest

from day03.input import parse_input


class TestParseInput(unittest.TestCase):
    def test_something(self):
        data = parse_input('./input/test1.txt')
        self.assertEqual(10, len(data))
        self.assertEqual(10, len(data[0]))
        self.assertEqual('.', data[9][9])


if __name__ == '__main__':
    unittest.main()
