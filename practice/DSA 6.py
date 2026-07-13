# Find the largest and smallest numbers in a list in a single loop

nums = [12 , 5 , 8 , 20 , 1 , 15]

largest_number = nums[0]
smallest_number = nums[0]

for num in nums:
    if num > largest_number:
        largest_number = num
    if num < smallest_number:
        smallest_number = num

print(smallest_number,largest_number)