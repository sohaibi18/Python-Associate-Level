from datetime import datetime


def amount(deposits, logged_in_user):
    while True:
        if logged_in_user:
            print("1. To See the Record  2. To enter new Deposit")
            choice = int(input("You want to see the deposits record or enter new deposit ??"))
            if choice == 1:
                print("Your deposits record: ", deposits[logged_in_user])
            elif choice == 2:
                deposit = int(input("Enter the amount you want to deposit"))
                date_of_deposit = datetime.now().strftime("%Y-%m-%d")
                if logged_in_user in deposits:
                    deposits[logged_in_user]["deposit"].append((deposit, date_of_deposit))
                    print("Your deposits record: ", deposits[logged_in_user])
                    break
                else:
                    print("Invalid Entry")
            else:
                print("Invalid Entry")
        else:
            print("You are not the registered user, Kindly registered yourself and then access the system")

