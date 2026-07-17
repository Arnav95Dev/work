# Reverse a number without converting it to a string

def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = (rev * 10) + digit
        n = n // 10

    return rev

num = int(input("Enter a number : "))

print(f"The reversed number is : {reverse_number(num)}")