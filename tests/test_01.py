import unittest
from p01.b import find_all_occurrences


class Test01(unittest.TestCase):

    def test_find_all_occurrences(self):
        # Test an example where the word occurs multiple times in the line
        word = "test"
        line = "this is a test line for testing the find_all_occurrences method"
        results = list(find_all_occurrences(word, line))
        self.assertListEqual(results, [10, 24])

        # Test an example where the word does not occur in the line
        word = "python"
        results = list(find_all_occurrences(word, line))
        self.assertListEqual(results, [])

        # Test an example where the word is the first word in the line
        word = "this"
        results = list(find_all_occurrences(word, line))
        self.assertListEqual(results, [0])

        # Test an example where the word is the last word in the line
        word = "method"
        results = list(find_all_occurrences(word, line))
        self.assertListEqual(results, [57])


if __name__ == '__main__':
    unittest.main()
