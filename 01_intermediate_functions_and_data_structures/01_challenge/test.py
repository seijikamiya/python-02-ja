import unittest
from extract_data import extract_data, better_extract_data


class TestExtractData(unittest.TestCase):
    def test_string(self):
        self.assertEqual(
            extract_data(
                "User details: Name:John. He is very active. He is also quite tall, standing at Height:181cm. He is Age:30, and spends his time as an Occupation:Engineer. End of data."
            ),
            ["Name:John", "Height:181cm", "Age:30", "Occupation:Engineer"],
        )

    def test_empty_string(self):
        self.assertEqual(extract_data(""), [])


class TestBetterExtractData(unittest.TestCase):
    def test_string(self):
        self.assertEqual(
            better_extract_data(
                "User details: Name:John. He is very active. He is also quite tall, standing at Height:181cm. He is Age:30, and spends his time as an Occupation:Engineer. End of data."
            ),
            [
                ("Name", "John"),
                ("Height", "181cm"),
                ("Age", "30"),
                ("Occupation", "Engineer"),
            ],
        )

    def test_empty_string(self):
        self.assertEqual(better_extract_data(""), [])


if __name__ == "__main__":
    unittest.main()
