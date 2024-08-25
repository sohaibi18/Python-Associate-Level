def borrowbook(inventory, borrowedbooks, booktitle):
    if booktitle in inventory and booktitle not in borrowedbooks:
        borrowedbooks.append(booktitle)
        inventory.remove(booktitle)
        print(f"Book '{booktitle}' has been borrowed.")
    elif booktitle in borrowedbooks:
        print(f"Book '{booktitle}' is already borrowed.")
    else:
        print(f"Book '{booktitle}' is not available in the inventory.")
