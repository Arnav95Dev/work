# Find the difference between the largest and smallest number

nums = [4 , 7 , 2 , 9 , 5 , 1]

largest_number = nums[0]
smallest_number = nums[0]

for num in nums:
    if num > largest_number :
        largest_number = num

    if num < smallest_number:
        smallest_number = num

diff = largest_number - smallest_number

print(f"The difference between largest number and smallest number is {diff}")