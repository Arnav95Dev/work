# Write a function largest(a,b,c) that return the largest of the three numbers
def largest(a,b,c):
    if a >= b and a >= c :
        return a
    
    elif b >= a and b >= c :
        return b
    
    else: 
        return c
    
n1 = int(input("Enter a number : "))
n2 = int(input("Enter a number : "))
n3 = int(input("Enter a number : "))

print(f"The largest number out of these are : {largest(n1,n2,n3)}")