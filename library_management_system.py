class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")


class Member(Person):
    def __init__(self, name, age, member_id, borrowed_books=0):
        super().__init__(name, age)
        self.member_id = member_id
        self.borrowed_books = borrowed_books

    def borrow_book(self):
        self.borrowed_books += 1

    def return_book(self):
        self.borrowed_books -= 1

    def display_info(self):  # Override
        print(
            f"Member ID\t: {self.member_id}\nName\t: {self.name}\nAge\t: {self.age}\nBorrowed Books\t: {self.borrowed_books}")


class Book:
    def __init__(self, title, author, isbn, status=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def display_book(self):
        print(
            f"ISBN\t: {self.isbn}\nTitle\t: {self.title}\nAuthor\t: {self.author}")
        if self.status == True:
            print(f"Status\t: Available")
        else:
            print(f"Status\t: Borrowed")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        print("\n----- Add New Book -----\n")
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        try:
            isbn = input("Enter ISBN: ")
            if self.books != []:
                book_isbn = [item[2] for item in self.books]
                if isbn in book_isbn:
                    raise Exception("\nError: ISBN already exists.\n")
                book = Book(title, author, isbn, True)
                self.books.append(
                    [book.title, book.author, book.isbn, book.status])
            else:
                book = Book(title, author, isbn, True)
                self.books.append(
                    [book.title, book.author, book.isbn, book.status])
        except Exception as e:
            print(e)
        else:
            print("\nBook added successfully!\n")

    def register_member(self):
        print("\n----- Register Member -----\n")
        try:
            member_id = input("Enter Member ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))

            if self.members != []:
                allmember_id = [item[2] for item in self.members]
                if member_id in allmember_id:
                    raise Exception("\nError: Member ID already exists.\n")

            if age < 0:
                raise Exception("\nError: Age must be greater than 0.\n")
            new_member = Member(name, age, member_id)
            self.members.append(
                [new_member.name, new_member.age, new_member.member_id, new_member.borrowed_books])
        except Exception as e:
            print(e)
        else:
            print("\nMember registered successfully!\n")

    def borrow_book(self):
        print("\n------ Borrow Book ------\n")
        try:
            member_id = input("Enter Member ID: ")
            isbn = input("Enter Book ISBN: ")
            book_isbn = [item[2] for item in self.books]
            if isbn not in book_isbn:
                raise Exception("\nBook not found.\n")
            book = list(filter(lambda item: item[2] == isbn, self.books))

            allmember_id = [item[2] for item in self.members]

            if member_id not in allmember_id:
                raise Exception("\nMember not found.\n")

            member = list(
                filter(lambda mem: mem[2] == member_id, self.members))
            if book[0][-1] == True:
                print("\nBook borrowed successfully.\n")
                book[0][-1] = False
                member[0][-1] += 1
            else:
                print("\nSorry! This book is currently unavailable.\n")
        except Exception as e:
            print(e)

    def return_book(self):
        print("\n------ Return Book ------\n")
        try:
            member_id = input("Enter Member ID: ")
            isbn = input("Enter Book ISBN: ")

            allmember_id = [item[2] for item in self.members]

            if member_id not in allmember_id:
                raise Exception("\nInvalid Member! Member not found.\n")

            member = list(
                filter(lambda mem: mem[2] == member_id, self.members))
            book = list(filter(lambda item: item[2] == isbn, self.books))
            if book[0][-1] == False:
                print("\nBook returned successfully.\n")
                book[0][-1] = True
                member[0][-1] -= 1
        except Exception as e:
            print(e)

    def show_books(self):
        print("\n------------- BOOK LIST -------------\n")
        for item in self.books:
            book = Book(item[0], item[1], item[2], item[3])
            book.display_book()
            print()
            print("-"*30)
            print()

    def show_members(self):
        print("\n----------- MEMBER LIST ------------\n")
        for mem in self.members:
            member = Member(mem[0], mem[1], mem[2], mem[3])
            member.display_info()
            print()
            print("-"*30)
            print()

    def search_book(self):
        print("\n------ Search Book ------\n")
        title = input("Enter Book Title: ")

        book = list(filter(lambda item: item[0] == title, self.books))

        if book != []:
            print("\nBook Found!\n")
            for item in book:
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
