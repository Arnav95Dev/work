# In this i will take the input from user and will find the greatest number using loops

numbers = []

for i in range(3):
    num = int(input("Enter a number : "))
    numbers.append(num)

largest_number = numbers[1]

for num in numbers:
    if num > largest_number:
        largest_number = num

print(f"The largest number you selected was {largest_number}")