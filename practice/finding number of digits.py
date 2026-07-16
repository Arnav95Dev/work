# Write a function def count_digits(n) Return the number of digits in a number

def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1

    return count

num = int(input("Enter a number : "))

print(f"Number of digits : {count_digits(num)}")