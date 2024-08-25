def addbook(inventory, booktitle):
    if booktitle not in inventory:
        inventory.append(booktitle)
        print(f"Book '{booktitle}' has been added to the inventory.")
    else:
        print(f"Book '{booktitle}' is already in the inventory.")

def removebook(inventory, booktitle):
    if booktitle in inventory:
        inventory.remove(booktitle)
        print(f"Book '{booktitle}' has been removed from the inventory.")
    else:
        print(f"Book '{booktitle}' is not in the inventory.")
