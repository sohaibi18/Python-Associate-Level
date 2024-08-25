def returnbook(inventory, borrowedbooks, booktitle):
    if booktitle in borrowedbooks:
        borrowedbooks.remove(booktitle)
        inventory.append(booktitle)
        print(f"Book '{booktitle}' has been returned to the inventory.")
    else:
        print(f"Book '{booktitle}' was not borrowed.")
