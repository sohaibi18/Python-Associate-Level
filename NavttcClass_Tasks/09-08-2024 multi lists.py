#shortcut for using for loop in multidimensional lists
# rest = 0
# noofdays = 30
# noofhours = 24
# noof_rests = [rest for i in (range(24),) for i in range(30)]#in python always take primarily the smallest value and than the largest value
# this below code is to print the matrix other words chessboard
# EMPTY = "-"
# ROOK = "R"
# Laptop = "L"
# board = []
#
# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)
#
# board[0][0] = ROOK
# board[0][7] = ROOK
# board[7][0] = ROOK
# board[7][7] = ROOK
# board[2][3] = Laptop
# for row in board:
#     for element in row:
#         print(element, end=" ")
#     print()

# import random
#
# temps = [[0.0 for h in range(24)] for d in range(31)]
# for d in range(31):
#     for h in range(24):
#         temps[d][h] = random.uniform(-10.0, 35.0)
# total = 0.0
#
# for day in temps:
#     total += day[11]
#
# average = total / 31
#
# print("Average temperature at noon:", average)
# highest = -100.0
# for day in temps:
#     for temp in day:
#         if temp > highest:
#             highest = temp
# print("The highest temperature was:", highest)
# hotdays = 0
# for day in temps:
#     if day[11] > 20.0:
#         hotdays += 1
# print("Hotdays are: ", hotdays)
# average1 = hotdays / 31
# print("The Average of noon: ", average1)


#Three dimensional Array program

number_of_buildings = 3
number_of_floors = 15
number_of_rooms_per_floor = 20
rooms = []

for t in range(number_of_buildings):
    building = []
    for f in range(number_of_floors):
        floor = [False for r in range(number_of_rooms_per_floor)]
        building.append(floor)
    rooms.append(building)

# 6. Make any three rooms as True on the 15th floor of the third building
rooms[2][14][0] = True  # Room 1 on the 15th floor of the 3rd building
rooms[2][14][1] = True  # Room 2 on the 15th floor of the 3rd building
rooms[2][14][2] = True  # Room 3 on the 15th floor of the 3rd building

# 7. Take a variable as vacancy should be equal to 0
vacancy = 0

# 8. Run for loop in range pass number of rooms per floor
for r in range(number_of_rooms_per_floor):

    # 9. If not rooms [][][], mention building, floor 15th and pass control variable as room
    if not rooms[2][14][r]:  # Checking if the room is False (i.e., vacant)

        # Print which room is vacant
        print(f"Building 3, Floor 15, Room {r + 1} is vacant.")

        # Increment vacancy by 1
        vacancy += 1

# 10. Print vacancies with a good message.
print(f"\nTotal number of vacant rooms on the 15th floor of the 3rd building: {vacancy}")








