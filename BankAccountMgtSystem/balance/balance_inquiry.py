def balance(deposits, logged_in_user):
    if logged_in_user:
        if logged_in_user in deposits:
            total_amount = sum(amount for amount, date in deposits[logged_in_user]['deposit'])
            print("Your Current Balance is: ", total_amount)
            exit()


