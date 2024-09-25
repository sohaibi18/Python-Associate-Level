# try:
#     stream = open(r"C:\Users\User\Desktop\file.txt", "rt")
#     # Processing goes here.
#     stream.close()
# except Exception as exc:
#     print("Cannot open the file:", exc)


# import errno
#
# try:
#     s = open("c:/users/user/Desktop/file.txt", "rt")
#     # Actual processing goes here.
#     s.close()
# except Exception as exc:
#     if exc.errno == errno.ENOENT:
#         print("The file doesn't exist.")
#     elif exc.errno == errno.EMFILE:
#         print("You've opened too many files.")
#     else:
#         print("The error number is:", exc.errno)

# from os import strerror
#
# try:
#     wcnt = lcnt = 0
#     s = open('c:/Users/Sohaib/Desktop/sohaib.txt', 'rt')
#     line = s.readline()
#
#     while line != '':
#         lcnt += 1
#         words = line.split()
#         wcnt += len(words)
#         for word in words:
#             print(word, end=' ')
#         line = s.readline()
#
#     s.close()
#     print("\n\nWords in file:     ", wcnt)
#     print("Lines in file:     ", lcnt)
# except IOError as e:
#     print("I/O error occurred:", strerror(e.errno))

# from os import strerror
#
# try:
#     ccnt = lcnt = 0
#     s = open('c:/Users/Sohaib/Desktop/sohaib.txt', 'rt')
#     lines = s.readlines(2)
#     while len(lines) != 0:
#         for line in lines:
#             lcnt += 1
#             for ch in line:
#                 print(ch, end='')
#                 ccnt += 1
#         lines = s.readlines(10)
#     s.close()
#     print("\n\nCharacters in file:", ccnt)
#     print("Lines in file:     ", lcnt)
# except IOError as e:
#     print("I/O error occurred:", strerror(e.errno))

# from os import strerror
#
# try:
#     ccnt = lcnt = 0
#     for line in open('c:/Users/Sohaib/Desktop/sohaib.txt', 'rt'):
#         lcnt += 1
#         for ch in line:
#             print(ch, end='')
#             ccnt += 1
#     print("\n\nCharacters in file:", ccnt)
#     print("Lines in file:     ", lcnt)
# except IOError as e:
#     print("I/O error occurred: ", strerror(e.errno))

# from os import strerror
#
# try:
#     fo = open('c:/Users/Sohaib/Desktop/sohaib1.txt', 'wt')  # A new file (newtext.txt) is created.
#     for i in range(10):
#         s = "line #" + str(i + 1) + "\n"
#         for ch in s:
#             fo.write(ch)
#     fo.close()
# except IOError as e:
#     print("I/O error occurred: ", strerror(e.errno))

from os import strerror

try:
    fo = open('c:/Users/Sohaib/Desktop/sohaib1.txt', 'wt')
    for i in range(10):
        fo.write("line #" + str(i+1) + "\n")
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

