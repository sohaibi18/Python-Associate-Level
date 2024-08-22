# Implement a system and apply all below functions using dictionary
# key(), sorted(), values(), items(),update(),popitem()


# Exceptions
# try:
#     def fun(num1, num2, operation):
#         operation = input("Enter Operations Symbol: ")
#         if operation == "+":
#             return num1 + num2
#         elif operation == "-":
#             return num1 - num2
#         elif operation == "/":
#             return num1 / num2
#         elif operation == "*":
#             return num1 * num2
#         else:
#             raise ValueError("Give the right inputs: ")
#
#
#     print(fun(2, 2, "operation"))
# except ZeroDivisionError as zde:
#     print(zde)
# except ValueError as ve:
#     print(ve)

def func(a, b, c):
    return a + b + c


while True:
    try:
        data1 = float(input("Enter value for Float 1: "))
        data2 = float(input("Enter value for Float 2: "))
        data3 = float(input("Enter value for Float 3: "))
        print("You have accessed the function: ")

        fun = func(data1, data2, data3)
        print(fun)

        choice = input("Do you want to perform the calculation again: ")
        choice.lower()
        if choice != 'Y':
            print("Good Bye")
            break
    except ValueError:
        print("There is a value error")
