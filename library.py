# Aggregation = Represents a relationship where one object (the whole)
#               contain references to one or more INDEPENDENT objects (the parts)
#               A relationship where one object contain references to other INDEPENDENT objects
#               "has-a" relationship

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]
    
class Books:
    def __init__(self, title, author):
        self.title = title
        self.author = author
