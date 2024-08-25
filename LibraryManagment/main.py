from inventory_operations.inventory import addbook, removebook
from borrow_operations.borrow import borrowbook
from return_operations.return_book import returnbook


def main():
    inventory = []
    borrowedbooks = []

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            booktitle = input("Enter the book title to add: ")
            addbook(inventory, booktitle)
        elif choice == 2:
            booktitle = input("Enter the book title to remove: ")
            removebook(inventory, booktitle)
        elif choice == 3:
            booktitle = input("Enter the book title to borrow: ")
            borrowbook(inventory, borrowedbooks, booktitle)
        elif choice == 4:
            booktitle = input("Enter the book title to return: ")
            returnbook(inventory, borrowedbooks, booktitle)
        elif choice == 5:
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice! Please try again.")

        print("\nCurrent Inventory:", inventory)
        print("Borrowed Books:", borrowedbooks)


if __name__ == "__main__":
    main()
