def account_info(customer_info):
    username = input("Enter username: ")
    password = int(input("Enter Password: "))
    if username in customer_info:
        if customer_info[username] == password:
            return username
        else:
            print("Wrong Password, Try Again")
    else:
        customer_info[username] = []
        customer_info[username].append(password)
        print("You are successfully added")
        print(customer_info)
        return username


def customer_name(customer_details, logged_in_user):
    if logged_in_user in customer_details:
        for key, value in customer_details[logged_in_user].items():
            print(f"{key} : {value}")
    else:
        print("You are not the authorized person")


def initial_deposit(initial_amount_deposit, logged_in_user):
    if logged_in_user:
        amount = int(input("How much amount initial amount you want to deposit: ")).strip()
        initial_amount_deposit[logged_in_user] = []
        initial_amount_deposit[logged_in_user].append(amount)
        print(initial_amount_deposit)
