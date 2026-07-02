name = str(input("Enter your name :"))
age = int(input("Enter your age: "))
branch = str(input("Enter your branch (in capital):"))
sem = int(input("Enter the semester: "))
student = {
    "name" : name ,
    "age" : age ,
    "branch" : branch , 
    "semester" : sem ,
}

print(student)
print(student["name"])
student.update({"semester" : 2})
student.update({"CGPA" : 9.3})
student.pop("age")
print(student)