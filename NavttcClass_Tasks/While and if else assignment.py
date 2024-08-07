

def studMgtSysLogo ():
    print("!", "*" * 25, "!")
    print("! STUDENT \t \t \t MANAGEMENT \t \t \t SYSTEM !")
    print("!", "*" * 25, "!")


def studMgtSys ():
    studentName = input("Enter Student Name")
    studentFatherName = input("Enter Student Father Name")
    studentAddress = input("Enter Student Address")
    studentContactNo = input("Enter Student Contact Number")
    print(f"Student Name is {studentName}, Father Name is", studentFatherName)


def marks():
    english = int(input("Enter marks for english"))
    science = int(input("Enter marks for science"))
    urdu = int(input("Enter marks for urdu"))
    totalMarks = 500
    obtainedMarks = english + science + urdu
    percentage = (obtainedMarks / totalMarks) * 100
    print(f"Obtained Marks are {obtainedMarks}, Percentage is", percentage)

def grade():
    english = int(input("Enter marks for english"))
    science = int(input("Enter marks for science"))
    urdu = int(input("Enter marks for urdu"))
    totalMarks = 500
    obtainedMarks = english + science + urdu
    percentage = (obtainedMarks / totalMarks) * 100
    if percentage>=80:
        print("Grade A" + "Percentage is",percentage)
    elif percentage>=70:
        print("Grade B"+ "Percentage is",percentage)
    elif percentage>=60:
        print("Grade C"+ "Percentage is",percentage)
    elif percentage>=50:
        print("Grade D"+ "Percentage is",percentage)
    else:
        print("Fail"+ "Percentage is",percentage)
studMgtSysLogo()
while True:

    print("1. for date \n 2. for subjects \n 3. for grade \n 4. exit program")
    choice = int(input("Enter Your Choice"))
    if choice==1:
        studMgtSys()
    elif choice==2:
        marks()
    elif choice==3:
        grade()
    else:
        exit()



