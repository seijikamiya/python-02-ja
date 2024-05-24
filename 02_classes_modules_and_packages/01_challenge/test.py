import unittest
from library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        self.library = Library()
        return super().setUp()

    def test_add_book(self):
        data = {"title": "1984", "author": "George Orwell"}

        self.library.add_book(
            title=data["title"],
            author=data["author"],
        )

        books = self.library.retrieve_books()

        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["title"], data["title"])
        self.assertEqual(books[0]["author"], data["author"])

    def test_remove_book(self):
        """Note: No error handling is expected."""

        data = {"title": "1984", "author": "George Orwell"}

        self.library.add_book(
            title=data["title"],
            author=data["author"],
        )

        self.library.remove_book(data["title"])

        self.assertEqual(len(self.library.retrieve_books()), 0)

    def test_retrieve_books(self):
        data = [
            {"title": "1984", "author": "George Orwell"},
            {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
        ]

        for book in data:
            self.library.add_book(
                title=book["title"],
                author=book["author"],
            )

        books = self.library.retrieve_books()

        self.assertEqual(len(books), len(data))

        for i, book in enumerate(books):
            self.assertEqual(book["title"], data[i]["title"])
            self.assertEqual(book["author"], data[i]["author"])

    def test_retrieve_books_empty(self):
        self.assertEqual(len(self.library.retrieve_books()), 0)

    def tearDown(self) -> None:
        self.library = None
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
