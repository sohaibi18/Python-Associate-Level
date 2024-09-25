# try:
#     stream = open(r"C:\Users\User\Desktop\file.txt", "rt")
#     # Processing goes here.
#     stream.close()
# except Exception as exc:
#     print("Cannot open the file:", exc)


import errno

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)
