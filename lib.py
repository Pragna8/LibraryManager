class Book:
    def __init__(self, title, copies, book_id, author, publication_year):
        self.title = title
        self.copies = copies
        self.id = book_id
        self.author = author
        self.publication_year = publication_year

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.id = member_id

class Loan:
    def __init__(self, book_id, member_id, lend_date, return_date):
        self.book_id = book_id
        self.member_id = member_id
        self.lend_date = lend_date
        self.return_date = return_date

library_books = []
library_members = []
library_loans = []

def add_book():
    print("\n")
    if len(library_books) >= 100:
        print("\033[0;31m")
        print("\t\tLibrary is full. Cannot add more books.\n")
        return

    title = input("Enter the book title: ")
    copies = int(input("Enter the number of copies: "))
    book_id = int(input("Enter the book ID: "))
    author = input("Enter the author: ")
    publication_year = int(input("Enter the publication year: "))

    new_book = Book(title, copies, book_id, author, publication_year)
    library_books.append(new_book)
    
    print("\033[0;32m")
    print("Book added successfully.\n")

def remove_book():
    print("\n")
    book_id = int(input("Enter the book ID: "))
    book_index = next((i for i, book in enumerate(library_books) if book.id == book_id), -1)

    if book_index == -1:
        print("\033[0;31m")
        print("Book not found.\n")
        return

    library_books.pop(book_index)
    print("\033[0;32m")
    print("Book removed successfully.\n")

def show_books():
    print("\n")
    if not library_books:
        print("\033[0;37m")
        print("No books available in the library.\n")
        return

    print("Books in the library:\n")
    for book in library_books:
        print("\033[0;37m")
        print(f"Title: {book.title}")
        print(f"Number of copies: {book.copies}")
        print(f"Book ID: {book.id}")
        print(f"Author: {book.author}")
        print(f"Publication year: {book.publication_year}\n")

def add_member():
    print("\n")
    if len(library_members) >= 100:
        print("\033[0;31m")
        print("Library member capacity reached. Cannot add more members.\n")
        return

    name = input("Enter the member name: ")
    member_id = int(input("Enter the member ID: "))

    new_member = Member(name, member_id)
    library_members.append(new_member)
    print("\033[0;32m")
    print("Member added successfully.\n")

def remove_member():
    print("\n")
    member_id = int(input("Enter the member ID: "))
    member_index = next((i for i, member in enumerate(library_members) if member.id == member_id), -1)

    if member_index == -1:
        print("\033[0;31m")
        print("Member not found.\n")
        return

    library_members.pop(member_index)
    print("\033[0;32m")
    print("Member removed successfully.\n")

def show_members():
    print("\n")
    if not library_members:
        print("\033[0;37m")
        print("No members in the library.\n")
        return

    print("Members in the library:\n")
    for member in library_members:
        print("\033[0;37m")
        print(f"Name: {member.name}")
        print(f"ID: {member.id}\n")

def lend_book():
    print("\n")
    book_id = int(input("Enter the book ID: "))
    member_id = int(input("Enter the member ID: "))

    book_index = next((i for i, book in enumerate(library_books) if book.id == book_id), -1)
    member_index = next((i for i, member in enumerate(library_members) if member.id == member_id), -1)

    if book_index == -1:
        print("\033[0;31m")
        print("Book not found.\n")
        return

    if member_index == -1:
        print("\033[0;31m")
        print("Member not found.\n")
        return

    if library_books[book_index].copies <= 0:
        print("\033[0;31m")
        print("No copies of the book available.\n")
        return

    if len(library_loans) >= 100:
        print("\033[0;31m")
        print("Library loan capacity reached. Cannot lend more books.\n")
        return

    lend_date = input("Enter the lending date (dd-mm-yyyy): ")
    day, month, year = map(int, lend_date.split('-'))
    day += 15
    if day > 31:
        day -= 31
        month += 1
        if month > 12:
            month -= 12
            year += 1
    return_date = f"{day:02d}-{month:02d}-{year}"

    new_loan = Loan(book_id, member_id, lend_date, return_date)
    library_loans.append(new_loan)
    library_books[book_index].copies -= 1

    print("\033[0;32m")
    print("Book lent successfully.\n")

def return_book():
    print("\n")
    book_id = int(input("Enter the book ID: "))
    member_id = int(input("Enter the member ID: "))

    loan_index = next((i for i, loan in enumerate(library_loans) if loan.book_id == book_id and loan.member_id == member_id), -1)

    if loan_index == -1:
        print("\033[0;31m")
        print("No matching loan record found.\n")
        return

    book_index = next((i for i, book in enumerate(library_books) if book.id == book_id), -1)

    if book_index == -1:
        print("\033[0;31m")
        print("Book not found.\n")
        return

    member_index = next((i for i, member in enumerate(library_members) if member.id == member_id), -1)

    if member_index == -1:
        print("\033[0;31m")
        print("Member not found.\n")
        return

    library_books[book_index].copies += 1
    library_loans.pop(loan_index)
    print("\033[0;32m")
    print("Book returned successfully.\n")

def show_loans():
    print("\n")
    if not library_loans:
        print("\033[0;37m")
        print("No books currently on loan.\n")
        return

    print("Books currently on loan:\n")
    for loan in library_loans:
        book = next((book for book in library_books if book.id == loan.book_id), None)
        member = next((member for member in library_members if member.id == loan.member_id), None)
        if book and member:
            print("\033[0;37m")
            print(f"Book title: {book.title}")
            print(f"Member name: {member.name}")
            print(f"Member ID: {member.id}")
            print(f"Lending date: {loan.lend_date}")
            print(f"Return date: {loan.return_date}\n")

def main():
    books = [
        ("Introduction to Algorithms", 3, 1, "Ronald L. Rivesten", 2014),
        ("Algorithms Unlocked", 5, 2, "Thomas H. Cormen", 2004),
        ("The Algorithm Design Manual", 8, 3, "Steven S. Skiena", 2010),
        ("Data Structures and Algorithms Made Easy", 6, 4, "Narasimha Karumanchi", 2015),
    ]
    members = [
        ("SANTHOSH", 182),
        ("SIDDHU", 189),
        ("MAANYA", 188),
        ("THARUN", 216),
        ("VARSHINI", 242),
        ("HARSHA", 236),
    ]
    
    for title, copies, book_id, author, year in books:
        library_books.append(Book(title, copies, book_id, author, year))
    
    for name, member_id in members:
        library_members.append(Member(name, member_id))

    while True:
        print("\033[0;36m")
        print("Library Management System")
        print("1. Add book")
        print("2. Remove book")
        print("3. Show books")
        print("4. Add member")
        print("5. Remove member")
        print("6. Show members")
        print("7. Lend book")
        print("8. Return book")
        print("9. Show loans")
        print("0. Exit\n")

        choice = int(input("Enter your choice: "))
        print("\n")

        if choice == 1:
            add_book()
        elif choice == 2:
            remove_book()
        elif choice == 3:
            show_books()
        elif choice == 4:
            add_member()
        elif choice == 5:
            remove_member()
        elif choice == 6:
            show_members()
        elif choice == 7:
            lend_book()
        elif choice == 8:
            return_book()
        elif choice == 9:
            show_loans()
        elif choice == 0:
            print("Exiting program. see you again..!\n")
            break
        else:
            print("Invalid choice. Please try again.\n")

        print("\n")

if __name__ == "__main__":
    main()
