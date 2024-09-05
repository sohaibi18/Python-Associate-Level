import random


class HotelMgtSys:
    def __init__(self, rooms, challans):
        occupied = False

    def checkin(self):
        print("Dear Customer before allocation of room you have to pay Rs 1000/- in advance")
        print("1. To enter challan number  2. To generate a challan")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            # def vouchers():
                voucher = int(input("Kindly enter the challan number through which you have paid the advance to "
                                    "verify: "))
                if voucher in challans:
                    advance = int(input("Enter the amount: "))
                    if advance >= 1000:
                        print(f"Amount {advance} is deposited")
                        checkin = int(input("Enter the room you want to checkin: "))
                        if checkin in rooms:
                            print("Sorry, the room is already occupied")
                        else:
                            rooms.append(checkin)
                            print(f"The {checkin} room is alloted to you")
                            print(f"The updated list of rooms are {rooms}")
                    else:
                        print("Sorry! Minimum 1000 has to be paid")
                else:
                    print("Sorry! you cannot checkin")
        elif choice == 2:
            obj_HotelMgtSys.advance()
        else:
            print("Invalid Entry")

    def checkout(self):
        checkout = int(input("Enter the room you want to checkout: "))
        if checkout in rooms:
            rooms.remove(checkout)
            print(f"The {checkout} is removed")
            print(f"The updated list of rooms are {rooms}")
        else:
            print("Invalid Entry")

    def status(self):
        checkstatus = int(input("Enter the room number to check the status of the room: "))
        if checkstatus in rooms:
            print("Room is resereved or occupied")
        else:
            print("Room is Empty")

    def advance(self):
        nic_number = input("Enter CNIC number without dashes to generate a challan: ")
        if len(nic_number) == 13 and nic_number.isdigit():
            global challan
            challan = random.randint(000000, 999999)
            challans.append(challan)
            print("Your Challan Number is:", challan)
            #self.checkin()
        else:
            print("Invalid CNIC Number")


challans = []
rooms = [10, 15, 20]
print("Welcome to Hotel Management System")
while True:
    obj_HotelMgtSys = HotelMgtSys(rooms, challans)
    print("1. Check the Status   2. Check - In   3. Check - Out  4. Generate Challan for checkin  5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj_HotelMgtSys.status()
    elif choice == 2:
        obj_HotelMgtSys.checkin()
    elif choice == 3:
        obj_HotelMgtSys.checkout()
    elif choice == 4:
        obj_HotelMgtSys.advance()
    else:
        print("Good Bye!")
        break
