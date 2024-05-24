import unittest
from apply_discount import apply_discount


class TestApplyDiscount(unittest.TestCase):
    def test_data(self):
        self.assertEqual(
            apply_discount(
                [
                    {"name": "Laptop", "category": "Electronics", "price": 1200},
                    {"name": "Bread", "category": "Food", "price": 2},
                    {"name": "Jacket", "category": "Apparel", "price": 100},
                ],
                50,
                10,
            ),
            [("Laptop", 1080.0), ("Jacket", 90.0)],
        )

    def test_no_data(self):
        self.assertEqual(apply_discount([], 50, 10), [])


if __name__ == "__main__":
    unittest.main()
