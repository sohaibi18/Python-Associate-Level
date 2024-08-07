import os


def license_mgt_sys():
    with open('LMS_DB.txt', 'w') as file:
        file.write("                                                    !" + "^" * 50 + "!\n")
        file.write("                                                    !{:^50}!\n".format("WELCOME TO"))
        file.write("                                                    !{:^50}!\n".format("LICENSE MANAGEMENT SYSTEM"))
        file.write("                                                    !" + "^" * 50 + "!\n\n")
        file.write("{:<10} {:<15} {:<15} {:<15} {:<20} {:<20} {:<15} {:<12} {:<12} {:<10} {:<15}\n".format(
            "Id", "FBO_Name", "Father_Name", "Contact_No", "Premises_Address", "License_Category",
            "License_Fee", "Issue_Date", "Expire_Date", "Add_By", "Bank_Challan_No"
        ))


def get_next_id():
    with open('LMS_DB.txt', 'r') as file:
        records = file.readlines()
        for record in reversed(records[1:]):  # read the records in reverse order and using [1:] skip in the
            # first line that is header
            record = record.strip()  # this ensure that line is not empty it contain record
            if record:
                try:
                    lastid = int(record.split()[0])  # this function split the record based on spaces between
                    # Then and [0] indicates the first integer character
                    return lastid + 1
                except ValueError:
                    continue  # Here rest of the lines are skipped because they are not converted to integer
    return 1  # by default, it returns 1 if no record is found


def select_license_category():
    categories = ['Restaurant', 'Hotel', 'Industry', 'General Store', 'Meal on Wheels']
    print("Select License Category:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    choice = int(input("Enter your choice (1-5): "))
    return categories[choice - 1]


def add_application():
    Id = get_next_id()
    FBOName = input("Enter FBO Name: ")
    FBOFatherName = input("Enter FBO Father Name: ")
    FBOContactNo = input("Enter FBO Contact Number: ")
    FBOAddress = input("Enter FBO Premises Address: ")
    LicCategory = select_license_category()
    LicenseFee = input("Enter License Fee: ")
    IssueDate = input("Enter Issue Date: ")
    ExpireDate = input("Enter Expire Date: ")
    AddBy = input("Enter Added By: ")
    BankChallanNo = input("Enter Bank Challan No: ")

    with open('LMS_DB.txt', 'a') as file:
        file.write("{:<10} {:<15} {:<15} {:<15} {:<20} {:<20} {:<15} {:<12} {:<12} {:<10} {:<15}\n".format(
            Id, FBOName, FBOFatherName, FBOContactNo, FBOAddress, LicCategory,
            LicenseFee, IssueDate, ExpireDate, AddBy, BankChallanNo
        ))


def show_record():
    with open('LMS_DB.txt', 'r') as file:
        records = file.readlines()
        Id = input("Enter the Id Number: ")
        found = False  # It is a flag concept before loop which initially indicates that ID is not found that's why it goes down to the loop for iterations
        for record in records[1:]:
            if record.strip():
                columns = record.split()
                if columns[0] == Id:
                    print("Record found:")
                    print("Id:", columns[0])
                    print("FBO Name:", columns[1])
                    print("Father Name:", columns[2])
                    print("Contact No:", columns[3])
                    print("Premises Address:", columns[4])
                    print("License Category:", columns[5])
                    print("License Fee:", columns[6])
                    print("Issue Date:", columns[7])
                    print("Expire Date:", columns[8])
                    print("Added By:", columns[9])
                    print("Bank Challan No:", columns[10])
                    found = True  # Instead of found we can also use the return function but found is more efficient
                    break
        if not found:
            print("Record not found.")


def update_record():
    Id = input("Enter the Id Number of the record you want to update: ")
    updated = False
    with open('LMS_DB.txt', 'r') as file:
        records = file.readlines()
    with open('LMS_DB.txt', 'w') as file:
        for record in records:
            print(record.strip())
            if record.startswith("!") or record.startswith("Id"):
                file.write(record)
                continue
            columns = record.split()
            if len(columns) < 11:  # Check if the record has enough columns
                file.write(record)
                continue

            print(f"Processing record: {columns}")
            if columns[0] == Id:
                print("Record found. Enter new details:")
                columns[1] = input("Enter new FBO Name: ") or columns[1]
                columns[2] = input("Enter new Father Name: ") or columns[2]
                columns[3] = input("Enter new Contact No: ") or columns[3]
                columns[4] = input("Enter new Premises Address: ") or columns[4]
                columns[5] = input("Enter new License Category: ") or columns[5]
                columns[6] = input("Enter new License Fee: ") or columns[6]
                columns[7] = input("Enter new Issue Date: ") or columns[7]
                columns[8] = input("Enter new Expire Date: ") or columns[8]
                columns[9] = input("Enter new Added By: ") or columns[9]
                columns[10] = input("Enter new Bank Challan No: ") or columns[10]

                updated_record = "{:<10} {:<15} {:<15} {:<15} {:<20} {:<20} {:<15} {:<12} {:<12} {:<10} {:<15}\n".format(
                    columns[0], columns[1], columns[2], columns[3], columns[4], columns[5], columns[6], columns[7],
                    columns[8],
                    columns[9], columns[10])
                file.write(updated_record)
                updated = True
            else:
                file.write(record)

    if updated:
        print("Record updated successfully.")
    else:
        print("Record not found.")


def delete_record():
    Id = input("Enter the Id Number of the record you want to delete: ")
    deleted = False

    # Read all records from the file
    with open('LMS_DB.txt', 'r') as file:
        records = file.readlines()

    with open('LMS_DB.txt', 'w') as file:
        for record in records:
            # Write header and separator lines back to the file
            if record.startswith("!") or record.startswith("Id"):
                file.write(record)
                continue

            columns = record.split()
            if len(columns) < 11:
                file.write(record)
                continue

            if columns[0] == Id:
                deleted = True
                continue  # Skip writing this record (effectively deleting it)

            # Write non-deleted records back to the file
            file.write(record)

    if deleted:
        print("Record deleted successfully.")
    else:
        print("Record not found.")


def main_menu():
    license_mgt_sys()
    while True:
        print("\nMain Menu:")
        print("1. Add New Application for License")
        print("2. Show Record of the FBO and Premises")
        print("3. Update Record of the FBO and Premises")
        print("4. Delete Record of the FBO and Premises")
        print("5. Exit Program")
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            add_application()
        elif choice == 2:
            show_record()
        elif choice == 3:
            update_record()
        elif choice == 4:
            delete_record()
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main_menu()
