class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def book_info(self):
        return (f'{self.title}, {self.author}, {self.year}')

class BookManager:
    def __init__(self):
        self.books = []
    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)
        print(f' {new_book.book_info()} is added. ')
    def all_books(self):
        if self.books != []:
            for book in self.books:
                print(book.book_info())
        else:
            print("There is no book in library.")

    def search_book(self, title):
        searched_books = []
        for i in self.books:
            if title == i.title:
                searched_books.append(i)
        if searched_books != []:
            print(f"Book found: \n {i.book_info()}")
        else:
            print(f'Theres no book with this title : {title}.')
            
def choice_input():
    try:
        while True:
            choice = int(input("What would you like to do? \n 1 - add book \n 2 - view all books \n 3 - search book by title \n 4 - exit \n"))
            return choice
    except ValueError:
        return None

def manager():
    print("Welcome to the Book Manager!")
    manager = BookManager()
    while True:
        choice = choice_input()
        if choice == 1 :
            title = input("Enter a title of the book: ")
            author = input("Enter author of the book: ")
            while True:
                year = input("Enter the year book was published: ")
                if year.isdigit():
                    break                   
                else:
                    print("Please enter valid year!")
                    
            manager.add_book(title,author,year)
        elif choice == 2:
            manager.all_books()
        elif choice == 3:
            title = input("Enter a title of the book: ")
            manager.search_book(title)
        elif choice == 4:
            print("Thanks for using Book manager! Goodbye!")
            break
        else:
            print("Please choose only numbers given: 1-4")
            
        
manager()

