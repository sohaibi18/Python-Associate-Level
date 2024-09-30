# from os import strerror
#
# srcname = input("Enter the source file name: ")
# try:
#     src = open(srcname, 'rb')
# except IOError as e:
#     print("Cannot open the source file: ", strerror(e.errno))
#     exit(e.errno)
#
# dstname = input("Enter the destination file name: ")
# try:
#     dst = open(dstname, 'wb')
# except Exception as e:
#     print("Cannot create the destination file: ", strerror(e.errno))
#     src.close()
#     exit(e.errno)
#
# buffer = bytearray(65536)
# total = 0
# try:
#     readin = src.readinto(buffer)
#     while readin > 0:
#         written = dst.write(buffer[:readin])
#         total += written
#         readin = src.readinto(buffer)
# except IOError as e:
#     print("Cannot create the destination file: ", strerror(e.errno))
#     exit(e.errno)
#
# print(total, 'byte(s) succesfully written')
# src.close()
# dst.close()

from os import strerror


# Function to check if two files are identical
def files_are_identical(file1, file2):
    try:
        f1 = open(file1, 'rb')
        f2 = open(file2, 'rb')

        while True:
            b1 = f1.read(65536)
            b2 = f2.read(65536)
            if b1 != b2:
                return False  # Files differ
            if not b1:  # Reached the end of both files
                break

        f1.close()
        f2.close()
        return True

    except IOError as e:
        print("I/O error occurred while comparing files:", strerror(e.errno))
        return False


srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)

dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, 'wb')
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)

buffer = bytearray(65536)
total = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("I/O error occurred during file copying:", strerror(e.errno))
    exit(e.errno)

print(total, 'byte(s) successfully written')
src.close()
dst.close()

# Check if the files are identical
if files_are_identical(srcname, dstname):
    print("The files are identical.")
else:
    print("The files are not identical.")

