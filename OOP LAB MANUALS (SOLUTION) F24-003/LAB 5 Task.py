class Item:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

class Book(Item):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def additional_info(self):
        print(f"Pages: {self.pages}")
class Magazine(Item):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number

    def additional_info(self):
        print(f"Issue Number: {self.issue_number}")

book = Book("The Great Gatsby", "F. Scott Fitzgerald", 218)
magazine = Magazine("National Geographic", "Multiple Authors", 12)

book.display_info()
book.additional_info()
magazine.display_info()
magazine.additional_info()