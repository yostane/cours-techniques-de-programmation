class Book:
    def __init__(self, nb_pages, title, author, isbn) -> None:
        self.nb_pages = nb_pages
        self.title = title
        self.author = author
        self.isbn = isbn
        self.marked_page = 0

    def mark_page(self, page):
        if 0 <= page < self.nb_pages:
            self.marked_page = page
        else:
            print(f"Impossible de marque la page {page}")


class Library:
    def __init__(self, books) -> None:
        self.books = books

    def list_authors_method_1(self):
        authors = []
        for book in self.books:
            authors.append(book.author)
        return authors

    def list_authors_method_2(self):
        """Utilisation de la 'compréhension' de listes"""
        return [book.author for book in self.books]

    def sum_of_marked_pages_method_1(self):
        sum = 0
        for book in self.books:
            sum += book.marked_page
        return sum

    def sum_of_marked_pages_method_2(self):
        return [book.marked_page for book in self.books].sum()


book1 = Book(
    190,
    "Matt Weisfeld",
    "Object-Oriented Thought Process, The (Developer's Library)",
    "978-0135181966",
)
book2 = Book(230, "Jon Bodner", "Learning Go", "978-1098139292")

book1.mark_page(-1)
book1.mark_page(800)
book1.mark_page(3)

book2.mark_page(200)

books = [
    book1,
    book2,
    Book(300, "Rob Mastrodomenico", "The Python Book", "978-1119573319"),
]
books[-1].mark_page(33)

library = Library(books)
