class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []
        self._books = []

    def add_contract(self, contract):
        self._contracts.append(contract)

    def add_book(self, book):
        self._books.append(book)

    def contracts(self):
        return self._contracts
    def books(self):
        return self._books
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []
        self._authors = []

    def add_contract(self, contract):
        self._contracts.append(contract)

    def add_author(self, author):
        self._authors.append(author)

    def contracts(self):
        return self._contracts 
    def authors(self):
        return self._authors
      


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise ValueError("not an author")
        
        if not isinstance(book, Book):
            raise ValueError("not a book")
        
        if not isinstance(date, str):
            raise ValueError("is not a string")
        
        if not isinstance(royalties, int):
            raise ValueError("isn't an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        author.add_contract(self)
        author.add_book(self.book)
        book.add_contract(self)
        book.add_author(self.author)
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]