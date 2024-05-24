import unittest

from mystery_function import mystery_function


class TestMysteryFunction(unittest.TestCase):
    def test_list_with_even_numbers(self):
        self.assertEqual(mystery_function([1, 2, 3, 4, 5]), [1, 4, 3, 16, 5])
        self.assertEqual(
            mystery_function([10, 21, 32, 43, 54]), [100, 21, 1024, 43, 2916]
        )

    def test_empty_list(self):
        self.assertEqual(mystery_function([]), [])

    def test_list_without_even_numbers(self):
        self.assertEqual(mystery_function([1, 3, 5]), [1, 3, 5])


if __name__ == "__main__":
    unittest.main()
