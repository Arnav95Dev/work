# Write a function is_even that returns True if the number is even otherwise false
num = int(input("Enter a number to check whether it is even or odd : "))

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
print(is_even(num))