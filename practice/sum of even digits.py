# write a function to find only the sum of even digits
def sum_even_digits(n):
    even = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        
        if digit % 2 == 0 :
            even += digit
    
    return even

num = int(input("Enter a number: "))

print(f"Sum of the even digits : {sum_even_digits(num)}")