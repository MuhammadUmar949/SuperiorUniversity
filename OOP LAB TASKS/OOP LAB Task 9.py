class Document:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


class Book(Document):
    def __init__(self, title, author, genre=None, pages=None):
        
        if genre is not None and pages is not None:
            self.genre = genre
            self.pages = pages
        else:
            self.genre = "Unknown"
            self.pages = 0
        
        super().__init__(title, author)
    
    def display_info(self):
        
        super().display_info()  
        print(f"Genre: {self.genre}")
        print(f"Pages: {self.pages}")
    
    def add_book_info(self, title, author, genre="Unknown", pages=0):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages


class Article(Document):
    def __init__(self, title, author, journal=None, doi=None):
        
        if journal is not None and doi is not None:
            self.journal = journal
            self.doi = doi
        else:
            self.journal = "Unknown"
            self.doi = "Unknown"
        
        super().__init__(title, author)
    
    def display_info(self):
        super().display_info()  
        print(f"Journal: {self.journal}")
        print(f"DOI: {self.doi}")
    
    def add_article_info(self, title, author, journal="Unknown", doi="Unknown"):
        self.title = title
        self.author = author
        self.journal = journal
        self.doi = doi


FILE_NAME = "documents.txt"

def save_documents(documents):
    """Saves books and articles information to a text file."""
    with open(FILE_NAME, "w") as file:
        for doc in documents:
            if isinstance(doc, Book):
                file.write(f"Book: {doc.title}, {doc.author}, {doc.genre}, {doc.pages}\n")
            elif isinstance(doc, Article):
                file.write(f"Article: {doc.title}, {doc.author}, {doc.journal}, {doc.doi}\n")
    print("Documents saved to file.")

def load_documents():
    """Reads documents from a text file."""
    documents = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                details = line.strip().split(", ")
                if "Book" in line:
                    documents.append(Book(details[1], details[2], details[3], int(details[4])))
                elif "Article" in line:
                    documents.append(Article(details[1], details[2], details[3], details[4]))
    except FileNotFoundError:
        print("No previous document records found.")
    return documents

def display_documents(documents):
    """Displays the list of books and articles."""
    if not documents:
        print("No documents available.")
    for doc in documents:
        doc.display_info()
        print("-" * 30)


def main():
    documents = load_documents()
    
    while True:
        print("\nDocument Management System")
        print("1. Display All Documents")
        print("2. Add New Book")
        print("3. Add New Article")
        print("4. Save and Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_documents(documents)
        
        elif choice == "2":
            title = input("Enter Book Title: ")
            author = input("Enter Author: ")
            genre = input("Enter Genre: ")
            pages = int(input("Enter Pages: "))
            book = Book(title, author, genre, pages)
            documents.append(book)
        
        elif choice == "3":
            title = input("Enter Article Title: ")
            author = input("Enter Author: ")
            journal = input("Enter Journal Name: ")
            doi = input("Enter DOI: ")
            article = Article(title, author, journal, doi)
            documents.append(article)
        
        elif choice == "4":
            save_documents(documents)
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
