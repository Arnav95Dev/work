physics = float(input("Enter the marks scored in physics?: "))
maths = float(input("Enter the marks scored in mathematics?: "))
chemistry = float(input("Enter the marks scored in chemistry?: "))
total = physics + chemistry+ maths
percent = (total / 300)*100
print(f" Total marks scored are: {total}")
print(f"tThe resulting percentage  are : {percent}")
if total >= 250 :
    print("Your grade is A")
elif total >=200 and total < 250 :
    print("Your grade is B")
elif total >= 150 and total < 200 :
    print("Your grade is C")
elif total >= 100 and total <150 :
    print("Your grade is D")
else :
    print("You are failed F")