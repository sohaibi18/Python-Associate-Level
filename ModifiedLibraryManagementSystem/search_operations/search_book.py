def search_book(noofcopies):
    book = input("Enter the name of a book you want to search ")
    if book in noofcopies:
        print(f"{book} Book is present having {noofcopies.get(book)} number of copies")
    else:
        print(f"{book}Book is not present")

