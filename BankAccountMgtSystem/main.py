from account_creation.create_account import account_info, customer_name, initial_deposit
from amount_deposit.deposit_amount import amount
from balance.balance_inquiry import balance
from withdraw_money.withdraw_amount import withdraw_money
from bankdatabase import customer_info, customer_details, initial_amount_deposit, deposits, withdraw_amounts


def main():
    logged_in = False
    logged_in_user = None
    print("!", "*" * 45, "!")
    print("! BANK \t \t \t MANAGEMENT \t \t \t SYSTEM !")
    print("!", "*" * 45, "!")
    while True:
        if not logged_in:
            print("Login to your account")
            logged_in_user = account_info(customer_info)
            if logged_in_user:
                logged_in = True
                print("You are logged in")
            else:
                print("Please Try Again")
        else:
            print("Main Menu")
            print("1. Customer Details  2. Initial Amount to Deposit  3. Deposits Record  4. Current Balance  5. "
                  "Withdraw Amount")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                customer_name(customer_details, logged_in_user)
            elif choice == 2:
                initial_deposit(initial_amount_deposit, logged_in_user)
            elif choice == 3:
                amount(deposits, logged_in_user)
            elif choice == 4:
                balance(deposits, logged_in_user)
            elif choice == 5:
                withdraw_money(customer_details, logged_in_user, withdraw_amounts)
            else:
                print("Go")
                break


if __name__ == "__main__":
    main()
