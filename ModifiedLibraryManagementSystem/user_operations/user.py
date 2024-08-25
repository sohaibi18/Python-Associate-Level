def add_user(users):
    username = input("Enter your username: ")
    if username in users:
        password = int(input("Enter your password: "))
        if users[username] == password:
            print("Welcome to LibMgtSys")
            return username
        else:
            print("Incorrect Password")
            return False
    else:
        print("Incorrect Credentials")
        return False
