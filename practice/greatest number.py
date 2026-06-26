# now i am going to find the greatest number among three numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
# main problem
if a>b and a>c:
    print(f"The greatest number is: {a}")
elif b>a and b>c:
    print(f"The greatest number is: {b}")
else:
    print(f"The greatest number is: {c}")