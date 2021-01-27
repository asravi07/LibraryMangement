# implement a student library system using oops where student can barrow a book from the list of books.
# + Cr/+eate a seperate library & student class. Your program must be menu driver. You are free to choose methods and
# atributes of your choice to implement the functionality.

class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks  # This is for displaying the list of books

    def displayAvailableBooks(self):
        print("Books present in this library are : ")
        for book in self.books:
            print("* "+book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been isused {bookName}. Please keep it safe and return it within 30 days.")
            self.books.remove(bookName)
            return True  # if the "if" condition is true then it will return true

        else:
            print(f"Sorry, This book is either not available or has already been isused to someone else.\nPlease wait unit the book is available. ")

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanx for returning this book I hope you enjoyed readint it. have a great day Ahead! ")

# student -------------------------


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow : ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return : ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["Vistas","Jungle Book","Flamingo", "vasant", "Honeycomb","Sumita Arora","Inception", "Matrix","Avengers", "King Kong"])

student = Student()

while (True):
    wlcm_Msg = "*********** WELCOME TO THE CENTRAL LIBRARY **************\n*Please Choose an option\n1. List of all the books\n2. Request a book \n3. Add/Return a book \n4. Exit Library" 
    print(wlcm_Msg)
    a = int(input("Enter a choice : "))
    if a == 1:
        centralLibrary.displayAvailableBooks()

    elif a == 2:
        centralLibrary.borrowBook(student.requestBook())

    elif a == 3:
        centralLibrary.returnBook(student.returnBook())

    elif a==4:
        print("Thanx for coming to the CENTRAL LIBRARY..")
        exit()
    else:
        print("Invalid Choice.")
