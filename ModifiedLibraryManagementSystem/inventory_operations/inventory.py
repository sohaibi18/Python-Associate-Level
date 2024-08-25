def add_book(inventory, noofcopies):
    book = input("Enter the Name of Book: ")
    if book not in inventory:
        inventory.append(book)
        noofcopies[book] = noofcopies.get(book, 0) + 1
        print(f"{book} is added in the inventory and no. of copies")
        print(inventory)
        print(noofcopies)


def remove_book(inventory, noofcopies):
    book = input("Enter the Name of Book you want to remove from the inventory: ")
    if book in inventory:
        inventory.remove(book)
        del noofcopies[book]
        print(inventory)
        print(noofcopies)
