# now this is the file where the challenge is lil bit harder

n1 = int(input("Enter a number : "))
n2 = int(input("Enter another number : "))
n3 = int(input("Enter another number : "))
n4 = int(input("Enter another number : "))
n5 = int(input("Enter another number : "))
n6 = int(input("Enter another number : "))
n7 = int(input("Enter another number : "))
n8 = int(input("Enter another number : "))
n9 = int(input("Enter another number : "))
n10 = int(input("Enter another number : "))

making_a_set = {n1 ,n2 , n3 , n4 , n5 , n6 , n7 , n8 , n9 , n10}

print(f"The unique numbers are : {making_a_set}")

user = int(input("Enter a number to search: "))

if user in making_a_set :
    print(f"{user} is present in the set")
else :
    print(f"{user} is not present in the set")