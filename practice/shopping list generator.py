a = int(input("Enter the amount of first item?"))
b = int(input("Enter the amount of second item?"))
c = int(input("Enter the amount of third item?"))

total = a + b + c
discount = total - (10*total)/100

if total > 1000 :
    print(f"Now you are going to get a  discount\nThe discounted price is {discount}")
else:
    print(f"Total amount is {total}")