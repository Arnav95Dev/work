present_students = {
    "rahul" : 92 ,
    "priya" : 88 ,
    "aman"  : 75 ,
    "riya"  : 95 ,
    "karan"  :81
}

student = input("Enter student name: ")
student = student.lower()

if student in present_students:
    print("Student is present!")
    marks = input("Do you want to see students marks(Y/N)")
    marks = marks.lower()
    if marks == "y":
        print(f"{student} has scored {present_students[student]}")
    elif marks == "n":
        print("Thanks for giving the feedback!")
    else:
        print("You have not type what was prescribed")
else:
    print("Student was absent")