class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []

    # Ajouter les méthodes ici
    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return
        print(f"Aucun livre \"{book_title}\" n'a été trouvé.")

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.borrow_books.append(book)
                self.books.remove(book)
                return
        print(f"Aucun livre \"{book_title}\" n'a été trouvé.")

    def return_book(self, book_title):
        for book in self.borrow_books:
            if book.title == book_title:
                self.books.append(book)
                self.borrow_books.remove(book)
                return
        print(f"Aucun livre \"{book_title}\" n'a été trouvé.")

    def available_books(self):
        title_list = []
        for book in self.books:
            title_list.append(book.title)
        return title_list

    def borrowed_books(self):
        title_list = []
        for book in self.borrow_books:
            title_list.append(book.title)
        return title_list
