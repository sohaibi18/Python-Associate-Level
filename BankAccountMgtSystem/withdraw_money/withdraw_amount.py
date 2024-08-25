from datetime import datetime


def withdraw_money(customer_details, logged_in_user, withdraw_amounts):
    if logged_in_user in customer_details:
        if logged_in_user not in withdraw_amounts:
            amount = int(input("Enter the amount you want to withdraw: "))
            current_date = datetime.now().strftime("%Y-%m-%d")
            if amount < int(customer_details[logged_in_user]["balance"]):
                remaining_balance = int(customer_details[logged_in_user]["balance"]) - amount
                print("The remaining balance is: ", remaining_balance)
                customer_details[logged_in_user]["balance"] = str(remaining_balance)
                print("Complete Record:", customer_details)
                withdraw_amounts[logged_in_user] = []
                withdraw_amounts[logged_in_user].append((amount, current_date))
                print("Total withdrawls Record ", withdraw_amounts)
            else:
                print("You don't have the sufficient balance")
                exit()
        else:
            customer_details[logged_in_user] = []
            amount = int(input("Enter the amount you want to withdraw: "))
            current_date = datetime.now().strftime("%Y-%m-%d")
            if amount < customer_details[logged_in_user]["balance"]:
                remaining_balance = customer_details[logged_in_user]["balance"] - amount
                print("The remaining balance is: ", remaining_balance)
                customer_details[logged_in_user]["balance"] = str(remaining_balance)
                print("Complete Record:", customer_details)
                withdraw_amounts[logged_in_user].append(amount, current_date)
                print("Total withdrawls Record ", withdraw_amounts)
                exit()
    else:
        print("Fill your customer details form and come again, Thanks")
        exit()
