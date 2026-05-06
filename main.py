class Book:
    def __init__(self, title, author, pages, code):
        self.title = title
        self.author = author
        self._pages = pages
        self.__code = code

    def read(self, pages):
        self._pages += pages
        print(f"Reading: {self._pages}")

    def bookmark(self, page):
        self._pages += page

    def info(self):
        print(f"Bookmark: {self._pages}")


b1 = Book("123", "asas", 5, "saashkahsckj")
b1.read(5)
b1.bookmark(40)
b1.info()
