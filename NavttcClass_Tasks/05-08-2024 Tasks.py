# import time
#
# # Write a for loop that counts to five.
# # Body of the loop - print the loop iteration number and the word "Mississippi".
# # Body of the loop - use: time.sleep(1)
#
# # Write a print function with the final message.
#
# for i in range(1, 6, 1):
#     print(i, "Mississippi")
#     time.sleep(2)
# print("Ready or not, Here I come!")

#========================================================
# largest_number = -99999999
# counter = 0
#
# while True:
#     number = int(input("Enter a number or type -1 to end program: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number
#
# if counter != 0:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")
#============================================================


# while True:
#     word = input("Enter the secret word: ")
#     if word == "chupacabra" or word == "CHUPACABRA":
#         break
# print("You have successfully left the loop")
#==========================================================

# user_word = input("Enter Your Word: ")
# user_word = user_word.upper()
# vowels = "AEIOU"
# not_vowels = ""
# for i in user_word:
#     if i in vowels:
#         continue
#     not_vowels += i
# print(not_vowels)
#==============================================================

# blocks = int(input("Enter the number of blocks: "))
# used_blocks = 0
# layer = 1
# while blocks >= used_blocks+layer:
#     used_blocks = used_blocks + layer
#     layer += 1
# print("The height of the pyramid:", layer-1)
# Initialization:
#
# blocks = 10
# used_blocks = 0
# layer = 1
# First Iteration:
#
# blocks >= used_blocks + layer -> 10 >= 0 + 1 -> True
# used_blocks = used_blocks + layer -> used_blocks = 0 + 1 -> used_blocks = 1
# layer += 1 -> layer = 2
# Second Iteration:
#
# blocks >= used_blocks + layer -> 10 >= 1 + 2 -> True
# used_blocks = used_blocks + layer -> used_blocks = 1 + 2 -> used_blocks = 3
# layer += 1 -> layer = 3
# Third Iteration:
#
# blocks >= used_blocks + layer -> 10 >= 3 + 3 -> True
# used_blocks = used_blocks + layer -> used_blocks = 3 + 3 -> used_blocks = 6
# layer += 1 -> layer = 4
# Fourth Iteration:
#
# blocks >= used_blocks + layer -> 10 >= 6 + 4 -> True
# used_blocks = used_blocks + layer -> used_blocks = 6 + 4 -> used_blocks = 10
# layer += 1 -> layer = 5
# Fifth Iteration:
#
# blocks >= used_blocks + layer -> 10 >= 10 + 5 -> False
# The loop exits.
# Output:
#
# print("The height of the pyramid:", layer - 1) -> print("The height of the pyramid:", 5 - 1) -> print("The height of the pyramid:", 4)
# The height of the pyramid with 10 blocks is 4.
#==========================================================
# c0 = int(input("Enter the Value: "))
# steps = 0
# while c0 != 1:
#     if c0 % 2 == 0:
#         c0 = c0 // 2
#     else:
#         c0 = 3 * c0 + 1
#     print(c0)
#     steps += 1
# print("Steps:", steps)
#========================================================






