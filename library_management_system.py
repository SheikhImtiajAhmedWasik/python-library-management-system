class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        pass


class Member(Person):
    def __init__(self, name, age, member_id, borrowed_books=""):
        super().__init__(name, age)
        self.member_id = member_id
        self.borrowed_books = borrowed_books  # here some work to do may be.

    def borrow_book(self):
        pass

    def return_book(self):
        pass

    def display_info(self):  # Override
        pass


class Book:
    def __init__(self, title, author, isbn, status):
        self.title = title
        self.author = author
        self.isbn = isbn
        if status == True:
            self.status = "Available"
        else:
            self.status = "Borrowed"

    def display_book(self):
        pass

    def check_status(self, isbn):  # include by myself
        # return Boolean value
        pass


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        print("\n----- Add New Book -----")
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        try:
            isbn = input("Enter ISBN: ")
            if self.books != []:
                book_isbn = [item[2] for item in self.books]
                if isbn in book_isbn:
                    raise Exception("Error: ISBN already exists.\n")
                book = Book(title, author, isbn, True)
                self.books.append([book.title, book.author, book.isbn, True])
            else:
                book = Book(title, author, isbn, True)
                self.books.append([book.title, book.author, book.isbn, True])
        except Exception as e:
            print(e)
        else:
            print("\nBook added successfully!\n")

    def register_member(self):
        print("\n----- Register Member -----")
        try:
            member_id = input("Enter Member ID: ")
            if self.members != []:
                allmember_id = [item[2] for item in self.members]
                if member_id in allmember_id:
                    raise Exception("Error: Member ID already exists.\n")

            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            if age < 0:
                raise Exception("Error: Age must be greater than 0.\n")
            new_member = Member(name, age, member_id)
            self.members.append(
                [new_member.name, new_member.age, new_member.member_id])
        except Exception as e:
            print(e)
        else:
            print("\nMember registered successfully!\n")

    def borrow_book(self):
        print("\n------ Borrow Book ------\n")
        try:
            member_id = input("Enter Member ID: ")
            isbn = input("Enter Book ISBN: ")

            allmember_id = [item[2] for item in self.members]

            if member_id not in allmember_id:
                raise Exception("\nInvalid Member! Member not found.\n")

            book = list(filter(lambda item: item[2] == isbn, self.books))
            if book[0][-1] == True:
                print("\nBook borrowed successfully.\n")
                book[0][-1] = False
            else:
                print("\nSorry! This book is currently unavailable.\n")
        except Exception as e:
            print(e)

    def return_book(self):
        pass

    def show_books(self):
        print("\n------------- BOOK LIST -------------\n")
        for item in self.books:
            print(
                f"ISBN\t: {item[2]}\nTitle\t: {item[0]}\nAuthor\t: {item[1]}")
            if item[3] == True:
                print("Status\t: Available\n")
            else:
                print("Status\t: Borrowed\n")
            print("-"*30)
            print()

    def show_members(self):
        pass

    def search_book(self):
        print("\n------ Search Book ------\n")
        title = input("Enter Book Title: ")

        book = list(filter(lambda item: item[0] == title, self.books))

        if book != []:
            print("\nBook Found!\n")
            for item in self.books:
                print(
                    f"ISBN\t: {item[2]}\nTitle\t: {item[0]}\nAuthor\t: {item[1]}")
                if item[3] == True:
                    print("Status\t: Available\n")
                else:
                    print("Status\t: Borrowed\n")
        else:
            print("\nBook not found.\n")


def main():
    lib = Library()
    while True:
        print("=" * 45)
        print("\tLIBRARY MANAGEMENT SYSTEM")
        print("=" * 45)
        print("1. Add Book\n2. Register Member\n3. Borrow Book\n4. Return Book\n5. Show All Books\n6. Show All Members\n7. Search Book\n8. Exi\n")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                lib.add_book()
            elif choice == 2:
                lib.register_member()
            elif choice == 3:
                lib.borrow_book()
            elif choice == 4:
                lib.return_book()
            elif choice == 5:
                lib.show_books()
            elif choice == 6:
                lib.show_members()
            elif choice == 7:
                lib.search_book()
            elif choice == 8:
                print("Thank you for using Library Management System.\nGoodbye!")
                break
            else:
                raise Exception("Invalid menu choice!")
        except Exception as e:
            print(e)

        input("Press Enter to continue....")


main()
