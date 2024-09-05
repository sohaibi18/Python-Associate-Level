#rfine() function

# def fun(path):
#     var = path.rfind("/")
#     if var != -1:
#         foundpath = path[var + 1:]
#     else:
#         foundpath = path
#     if not foundpath:
#         return "File not found"
#     return foundpath
#
#
# path = input("Enter the filename with path: ")
# print(fun(path))

#startswith () method


# filenames = input("Enter the file name: ")
#
# if filenames.startswith("data") or filenames.endswith(".txt"):
#     print("It is txt file")
# elif filenames.startswith("report") or filenames.endswith(".pdf"):
#     print("It is pdf file")
# elif filenames.startswith("image") or filenames.endswith(".jpg"):
#     print("It is image file")
# else:
#     print("Not found")

def mysplit(strng):
    strg = []
    var = ''
    for ch in strng:
        if ch == '':
            if var:
                strg.append(var)
                var = ''
        else:
            var += ch
    if var:
        strg.append(var)
    return strg





print(mysplit(strng="To be or not to be,that is the question"))
# print(mysplit(strng="   "))
# print(mysplit(strng=" abc "))
# print(mysplit(strng=""))
