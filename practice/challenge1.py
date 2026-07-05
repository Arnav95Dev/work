n1 = int(input("Enter a number! : "))
n2 = int(input("Enter another number! : "))
n3 = int(input("Enter another number! : "))
n4 = int(input("Enter another number! : "))
n5 = int(input("Enter another number! : "))
n6 = int(input("Enter another number! : "))
n7 = int(input("Enter another number! : "))
n8 = int(input("Enter another number! : "))
n9 = int(input("Enter another number! : "))
n10 = int(input("Enter another number! : "))
list = [n1 , n2 , n3 , n4 , n5 , n6 , n7 , n8 , n9 , n10]
list.sort()
largest = list[9]
smallest = list[0]
making_a_set = set(list)
adding = sum(making_a_set)

print(f"The unique numbers : {making_a_set}")
print(f"The largest number : {largest}")
print(f"The smallest number : {smallest}")
print(f"The sum of all the unique numbers : {adding}")