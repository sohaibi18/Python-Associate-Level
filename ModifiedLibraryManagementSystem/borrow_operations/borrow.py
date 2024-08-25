from datetime import timedelta, datetime

current_date = datetime.now()


def borrow_book(userborrowedbooks, noofcopies, logged_in_user, borrowedbooks, duedates):
    if len(userborrowedbooks.get(logged_in_user, [])) >= 3:
        print("You have reached the maximum limit. Kindly return any one book to borrow another book")
    else:
        print(f"{noofcopies} \nThese are the Books with their quantity present in the inventory")
        book = input("Enter the book you want to borrow: ")
        if book in noofcopies:
            borrowedbooks.append(book)
            noofcopies[book] = noofcopies.get(book, 0) - 1
            if logged_in_user not in userborrowedbooks:
                userborrowedbooks[logged_in_user] = []
            userborrowedbooks[logged_in_user].append(book)
            if logged_in_user not in duedates:
                duedates[logged_in_user] = []
            duedate = current_date + timedelta(days=7)
            duedates[logged_in_user].append(duedate.strftime("%Y-%m-%d"))
            print(borrowedbooks)
            print(noofcopies)
            print(userborrowedbooks)
            print(duedates)
