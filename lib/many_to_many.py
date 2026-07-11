class Author:
    all = []

    def total_royalties(self):
        return sum(
        contract.royalties
        for contract in self.contracts()
    )

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def contracts(self):
        return [
        contract
        for contract in Contract.all
        if contract.author == self
    ]

    def books(self):
        return [
        contract.book
        for contract in self.contracts()
    ]


    def __init__(self, name):

        self.name = name
        Author.all.append(self)


class Book:
    all = []

    def authors(self):
        return [
        contract.author
        for contract in self.contracts()
    ]

    def contracts(self):
        return [
        contract
        for contract in Contract.all
        if contract.book == self
    ]

    def __init__(self, title):
        self.title = title
        Book.all.append(self)


class Contract:
    all = []


    @classmethod
    def contracts_by_date(cls, date):
        return [
        contract
        for contract in cls.all
        if contract.date == date
    ]

    def __init__(self, author, book, date, royalties):

        if not isinstance(author, Author):
            raise Exception("author must be an Author")
        
        if not isinstance(book, Book):
            raise Exception("book must be a Book")


        if not isinstance(date, str):
            raise Exception("date must be a string")
        
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        
        Contract.all.append(self)