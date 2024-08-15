""" 
1. Design a Library Management System
Requirements:
Implement classes for Book, Member, Librarian, and Library.
Book should have attributes like title, author, ISBN, and status.
Member should have attributes like name, member_id, and a list of borrowed books.
Librarian should have attributes like name and employee_id.
Library should have a collection of books and methods to add/remove books, register members, lend books, and return books.

"""
class Book:
    def __init__(self,title,author, isbn):
        self.title =title
        self.author=author
        self.isbn=isbn
        self.status= 'available'

class Member:
    def __init__(self,name, member_id):
        self.name =name
        self.member_id=member_id
        self.borrowed_books=[]

    def borrow_book(self, book):
        if book.status =='available':
            book.status ='not available'
            self.borrowed_books.append(book)
            print("book borrowed ")
            
        else:
            print("book not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.status ='available'
            self.borrowed_books.remove(book)
            print("book returned")
        else:
            print("user does not have the book")

class Librarian:
    def __init__(self, name, employee_id):
        self.name =name
        self.employee_id =employee_id

class Library:
    def __init__(self):
        self.books =[]
        self.members =[]


    def add_book(self, book):
        self.books.append(book)
        print("book added")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn ==isbn:
                self.books.remove(book)
                print("Book removed")
                return
        print("Book not found")
        
    def register_member(self, member):
        self.members.append(member)
        print("Member Registered")

    def lend_book(self, isbn, member_id):
        for b in self.books:
            if b.isbn == isbn:
                book =b
            else:
                book = None
        for m in self.members:
            if m.member_id == member_id:
                member = m
            else:
                member = None
        if book and member:
            member.borrow_book(book)
        else:
            print("Book or member not found")

    def return_book(self, isbn, member_id):
        for b in self.books:
            if b.isbn == isbn:
                book =b
            else:
                book = None
        for m in self.members:
            if m.member_id == member_id:
                member = m
            else:
                member = None
        if book and member:
            member.return_book(book)
        else:
            print("Book or member not found")

    def display_status(self):
        print("\nLibrary Collection:")
        for book in self.books:
            print(f"'{book.title}' by {book.author} (ISBN: {book.isbn}) - Status: {book.status}")

        print("\nLibrary Members:")
        for member in self.members:
            borrowed_titles = [book.title for book in member.borrowed_books]
            print("Member:",member.name,"ID:",member.member_id,f" - Borrowed: {', '.join(borrowed_titles) if borrowed_titles else 'None'}")


library = Library()
librarian = Librarian("Aaa", "001")
print("Librarian: ",librarian.name,"Employee ID: ",librarian.employee_id)

book1 = Book("b1", "a1", "978")
book2 = Book("b2", "a2", "1234")
library.add_book(book1)
library.add_book(book2)
member1 = Member("M1", "101")
library.register_member(member1)

library.lend_book("978", "101")  #isbn, member id
library.display_status()

library.return_book("978", "01")
library.display_status()
