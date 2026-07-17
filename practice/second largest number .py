# Find the second largest number in a list without using sort()

nums = [12 , 45 , 7 , 89 , 34]

largest_number = nums[0]
second_largest_number = nums[0]

for num in nums:
    if num > largest_number:
        second_largest_number = largest_number
        largest_number = num

    if num < largest_number and num > second_largest_number:
        second_largest_number = num

print(second_largest_number)