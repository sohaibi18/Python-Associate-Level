#List

# b = [5, 3, 9, 6, "ALi"]
# print(b[-3::])

# a = [1, 2, 3, 4, 5]
# print("The List is: ", a)
# b = int(input("Enter the Value you want to replace: "))
# a[4] = b
# print("The Updated List is: ", a)
# del a[2]
# print("The Updated List after delete is: ", a)
#=================================================================

# my_list = []
# for i in range(5):
#     my_list.append(i + 1)
# print(my_list)
#=================================================================

# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# print("List a: ", a)
# print("List b: ", b)
# print("========================")
# a[3] = "Sohaib"
# b[3] = "Siddique"
# print("List a: ", a)
# print("List b: ", b)
# print("========================")
# b[2] = a[2]
# print("Updated List b: ", b)
# print("========================")
# del a[2]
# print("Updated List a: ", a)
# print("========================")
# name = input("Enter Value to be place in List a: ")
# a.insert(2, name)
# print("Newly Updated List a: ", a)
#
# print("Loop Task")
#
#
# def datainsert(list1):
#     i = 0
#     while i <= 5:
#         list1.insert(i, i + 1)
#         i += 1
#     print(list1)
#
#
# def dataappend(list2):
#     i = 0
#     while i <= 5:
#         list2.append(i)
#         i += 1
#     print(list2)
#
#
# list1 = []
# list2 = []
# datainsert(list1)
# dataappend(list2)

#=====================================================

beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(beatles)
for i in range(2):
    name = input("Enter the Name: ")
    beatles.append(name)
    print(beatles)
del beatles[3]
del beatles[3]
print(beatles)
beatles.insert(0, "Ringo Starr")
print(beatles)


