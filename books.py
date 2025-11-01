# Magic methods = Dunder method (double underscore) __init__, __str__, __eq__ etc
#                 They are automatically called by many of Python`s built-in operations.
#                 They allow developers to define or customize the behavior od objects

class Bookss:

    # CONSTRUCTOR METHOD
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # STRING METHOD
    def __str__(self):
        return f"'{self.title}' by {self.author} have {self.num_pages}"

    # EQUAL METHOD
    def __eq__(self, value):
        return self.title == value.title and self.author == value.author
    
    # LESS-THAN METHOD
    def __lt__(self, value):
        return self.num_pages < value.num_pages

    # GREATER-THAN METHOD
    def __gt__(self, value):
        return self.num_pages > value.num_pages

    # ADD METHOD
    def __add__(self, value):
        return self.num_pages + value.num_pages
    
    # SEARCH KEYWORD
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    # GET METHOD
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"