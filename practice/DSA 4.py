num = [5 , 2 , 9 , 1 , 7 , 3]

largest_number = num[0]
smallest_number = num[2]

for n in num:
    if n > largest_number:
        largest_number = n

else: 
    print(f"Largest number is saved {largest_number}")

for small in num:
    if small < smallest_number:
        smallest_number = small

else: 
    print(f"Smallest number is saved {smallest_number}")
