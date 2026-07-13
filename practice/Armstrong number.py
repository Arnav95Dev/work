number = int(input("Enter a number to check whether it is an armstrong number : "))
original_number = number

total = 0

while number > 0:
    last_digit = number % 10
    total += last_digit ** 3
    number = number // 10

print(total)

if original_number == total:
    print("It is an Armstrong number")

else:
    print("It is not an Armstrong number")