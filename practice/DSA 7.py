# To find the both second largest and second smallest number

nums = [12 , 5 , 8 , 20 , 1 , 15]

largest_number = nums[0]
smallest_number = nums[0]
second_largest_number = 0
second_smallest_number = 0


for num in nums :
    if num > largest_number:
        second_largest_number = largest_number
        largest_number = num
    
    elif num > second_largest_number:
        second_largest_number = num

    if num < smallest_number:
        second_smallest_number = smallest_number
        smallest_number = num

    elif num < second_smallest_number :
        second_smallest_number = num


print(largest_number,second_largest_number , second_smallest_number , smallest_number)