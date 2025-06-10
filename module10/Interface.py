from abc import ABC, abstractmethod

class Printable(ABC): #this is the interface withonly abstract method in it
    @abstractmethod
    def print_info(self):
        pass

class Book(Printable):
    def __init__(self, title, author):
        self.title=title
        self.author=author

    def print_info(self):
        print(f"Book;{self.title} by {self.author}")


libri=Book("Hija e Maleve", "Ismail Kadare")
libri.print_info()
