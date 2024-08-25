from user_operations.user import add_user
from inventory_operations.inventory import add_book, remove_book
from search_operations.search_book import search_book
from return_operations.return_book import return_book
from borrow_operations.borrow import borrow_book
from database import inventory, borrowedbooks, userborrowedbooks, users, noofcopies, duedates


def main():
    logged_in = False
    logged_in_user = None

    while True:
        if not logged_in:
            print("What do you want to do: ")
            print("1. Login to the LibMgtSys ")
            print("2. Exit ")
            choice = int(input("Enter Your Desired Action: "))
            if choice == 1:
                logged_in_user = add_user(users)
                if logged_in_user:
                    logged_in = True
                    print("You are now logged in")
                else:
                    print("Try Again")
            elif choice == 2:
                print("Exiting the System")
                break
            else:
                print("Invalid Choice")
        else:
            print("What do you want to do: ")
            print("1. Add a book in the inventory")
            print("2. Remove a book from the inventory")
            print("3. Search the books in inventory and their quantity")
            print("4. Borrow a book")
            print("5. Return a book")
            print("6. Exit the system")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_book(inventory, noofcopies)
            elif choice == 2:
                remove_book(inventory, noofcopies)
            elif choice == 3:
                search_book(noofcopies)
            elif choice == 4:
                borrow_book(userborrowedbooks, noofcopies, logged_in_user, borrowedbooks, duedates)
            elif choice == 5:
                return_book(borrowedbooks, noofcopies, userborrowedbooks, logged_in_user)
            else:
                print("Good Bye and Take Care")
                break


if __name__ == "__main__":
    main()
