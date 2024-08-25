def return_book(borrowedbooks, noofcopies, userborrowedbooks, logged_in_user):
    book = input("Enter the name of book you want to return: ")
    if book in borrowedbooks:
        borrowedbooks.remove(book)
        noofcopies[book] = noofcopies.get(book, 0) + 1
        userborrowedbooks[logged_in_user].remove(book)
        print(borrowedbooks)
        print(noofcopies)
        print(userborrowedbooks)
