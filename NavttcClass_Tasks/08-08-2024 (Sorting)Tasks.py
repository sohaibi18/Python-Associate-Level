# #Bubble Sort
# def bubble_sort(my_list):
#     NoofValue = len(my_list)
#     for i in range(NoofValue - 1):
#         for j in range(NoofValue - 1 - i):
#             if my_list[j] > my_list[j + 1]:
#                 my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
#     return my_list
#
#
# my_list = [8, 10, 6, 2, 4]
# bubble_sort(my_list)
# print(my_list)
# #========================Another Approach==========================
# my_list = [8, 10, 6, 2, 4]  # list to sort
# swapped = True  # It's a little fake, we need it to enter the while loop.
#
# while swapped:
#     swapped = False  # no swaps so far
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # a swap occurred!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#
# print(my_list)
#
# #============================Interactive Version of Bubble Sort=============
# my_list = []
# swapped = True
# num = int(input("How many elements do you want to sort: "))
#
# for i in range(num):
#     val = float(input("Enter a list element: "))
#     my_list.append(val)
#
# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#
# print("\nSorted:")
# print(my_list)
# #===============================Let python do the bubble sort===================
# my_list = [8, 10, 6, 2, 4]
# my_list.sort()
# print(my_list)
#=====================copying addresses of the list[] in a variable and access the list[] by that variable concept============
# list1 = [1, 2, 3, 4]
# list2 = list1
# print(list2)
# del list2[3]
# print(list1)
#=============================================For positive values=================================
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = list1[3:8]
# list3 = list1[4:]
# list4 = list1[1::2]
# list7 = list1[1:8:3]
# list5 = list1[1::]
# list6 = list1[:8]
#
# print("Printing specific part of list 1 (The ending point of slicing index 8 will not be print): ", list2)
# print("Printing values from index 4 to till end of list 1: ", list3)
# print("Printing values from index 1 till end by 2 step but actually on base of 2 only 1 value is skipped: ", list4)
# print("Printing values from index 1 to index 8 by 3 step and in result on base of 3, 2 values will skipped: ", list7)
# print("Printing Complete list by from index 1 till end: ", list5)
# print("Printing list of values before index 8: ", list6)
#=========================================For negative values====================================
from turtledemo.forest import start

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list10 = [11, 12, 13, 14, 15, 16, 17, 18, 19]
# list2 = list1[-8:-1]
# list3 = list1[-5:]
# list4 = list1[-2::-1]
# list7 = list1[-3:-8:-1]
# list5 = list1[-1::]
# list6 = list1[:-1]

# list1[start:len(list1)]
# list8 = list1
# print(list1)
# del list1[1:6]
# print(list1)

# print("Printing specific part of list 1 (The ending point of slicing index 8 will not be print): ", list2)
# print("Printing values from index 4 to till end of list 1: ", list3)
# print("Printing values from index 1 till end by 2 step but actually on base of 2 only 1 value is skipped: ", list4)
# print("Printing values from index 1 to index 8 by 3 step and in result on base of 3, 2 values will skipped: ", list7)
# print("Printing Complete list by from index 1 till end: ", list5)
# print("Printing list of values before index 8: ", list6)
#For deleting specific part in both the list and the variable to which list is assign
# list9 = list1
# del list9[1:5]
# print(list1)
# print(list9)

# del list1[:]
# print(list1)
# list1.append(10)
# list1.append(9)
# list1.append(8)
# print(list1)

# list1.append(list10)
# print(list1)
# print(list10)
# #======================finding largest value==========
#
# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
#
# for i in range(1, len(my_list)):
#     if my_list[i] > largest:
#         largest = my_list[i]
#
# print(largest)
# my_list = [1, 2, "Peshawar", 4, 10, "11000"]
# print(2 in my_list)
# print(1100 in my_list)
# print("Peshawr" not in my_list)
# print("Peshawar" not in my_list)

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)
        my_list = new_list

print("The list with unique elements only: ")
print(new_list)
print("The original list without duplicates: ", my_list)
