'''
TASK: Write a function that count number of odd and even digits 
'''

def count_even_odd_digits(n):
    odd = 0
    even = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        if digit % 2 == 0:
            even += 1
        

        else:
            odd += 1

    return even , odd

num = int(input("Enter a number : "))
even , odd = count_even_odd_digits(num)

print(f"Odd numbers : {odd}")
print(f"Even numbers : {even}")
