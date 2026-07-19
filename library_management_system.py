def main():
    while True:
        print("=" * 45)
        print("\tLIBRARY MANAGEMENT SYSTEM")
        print("=" * 45)
        print("1. Add Book\n2. Register Member\n3. Borrow Book\n4. Return Book\n5. Show All Books\n6. Show All Members\n7. Search Book\n8. Exi\n")

        choice = int(input("Enter your choice: "))

        if choice == 8:
            print("Thank you for using Library Management System.\nGoodbye!")
            break

        # all the next implementation will be here.

        input("Press Enter to continue....")


main()
