class Library:

    def __init__(self,lst):
        self.display_all_books = lst
        self.display_available_books = lst[:]
        self.books_lend = {} # key - books_name , value - user_nam

    def display_all(self):
        print("===DISPLAYING ALL BOOKS IN LIBRARY===")
        for c,book in enumerate(self.display_all_books):
            print(c+1,"." + book)
        print("==================")

    def display_available(self):
        print("===DISPLAYING AVAILABLE BOOKS IN LIBRARY===")
        for c,book in enumerate(self.display_available_books):
            print(c+1,"." + book)
        print("==================")

    def lend_books(self,name,book):
        print("===Book Borrowing===")
        #Correct Book name ?
        if book not in self.display_all_books:
            print("Check the book name")
            return
        #notes - log:
        if book in self.display_available_books:
            self.books_lend.update({book:name})
            self.display_available_books.remove(book)
            print("***You received the book :",book,"***")
        #if the borrowing book is not avaliable
        else:
            print("The book is already lend by",self.books_lend[book])
        print("==================")

    def return_book(self,book):
        print("===Returning Book===")
        if book not in self.display_all_books:
            print("Check the book name")
            return

        if book in self.display_all_books:
            self.display_available_books.append(book)
            print("**Book Returned***")
        print("==================")
            
        


#Creating an object for the library class


if __name__ == '__main__':
    print("//=======WeLcOmE TO LiBrArY//=======")
    lib = Library(['Rich Dad Poor Dad','Morning Miracles','Atomic Habits','The Life of pie'])


    #Setting menu:

    while True:
        print("1.Display All Books")
        print("2.Display Available Books")
        print("3.Borrow a Book")
        print("4.Return a Book")
        print("5.Quit")

        user_choice = int(input("Enter your choice:"))

        if user_choice == 1:
            lib.display_all()
        elif user_choice == 2:
            lib.display_available()
        elif user_choice == 3:
            name = input("User name:")
            book = input("Required Book name:")
            lib.lend_books(name,book)
        elif user_choice == 4:
            book = input("Enter the book name to return:")
        elif user_choice == 5:
            break
        else:
            print("Invalid Choice ! Try again....")
            





            
