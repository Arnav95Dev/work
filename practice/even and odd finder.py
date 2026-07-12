# using loops i will find even  and odd

nums = [12 , 5 , 8 , 20 , 1 , 15]

even = []
odd = []

for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(even)
print(odd)