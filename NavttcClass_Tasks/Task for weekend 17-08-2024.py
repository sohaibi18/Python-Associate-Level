# Implement a system and apply all below functions using dictionary
# key(), sorted(), values(), items(),update(),popitem()


# Exceptions

try:
    value = input("Enter Value: ")
    print(value)
except TypeError:
    print("It is type error")
except ZeroDivisionError:
    print("It is zero error")
except ValueError:
    print("It is value error")
except SyntaxError:
    print("It is syntax error")
except SystemError:
    print("System error")
except:
    print("Try Again")
