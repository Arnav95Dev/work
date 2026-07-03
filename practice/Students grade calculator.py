phy = int(input("How much marks did you scored in physics?: "))
bio = int(input("How much marks did you scored in biology?: "))
chem = int(input("How much marks did you scored in chemistry?: "))
math = int(input("How much marks did you scored in mathematics?: "))
eng = int(input("How much marks did you scored in english?: "))

# Now we are going to calculate its everything

marks = [phy , bio , chem , math , eng]

total = sum(marks)
percentage = (total/500)*100

print(f"Your total marks are {total}/500")
print(f"And you got {percentage} %")

if percentage >= 90 :
    print("Congrats you got an A grade!!!")
elif percentage <= 89 and percentage >= 75 :
    print("Congrats you got a B grade !")
elif percentage >= 60 and percentage <= 74 :
    print("You got a C grade...Try harder next time")
else:
    print("Your grade is D .... You need high improvement")