# finding the second largest number

nums = [12 , 5 , 8 , 20 , 1 , 15]

largest_number  = 0
second_largest_number = 0


for num in nums:
    if num > largest_number:
        small = largest_number
        largest_number = num
    elif num < largest_number and num > small:
        second_largest_number = num  

print(largest_number)
print(second_largest_number)