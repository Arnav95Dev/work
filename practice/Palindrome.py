
# num = str(input("Enter a number : "))

# reversed_num = num[::-1]

# if reversed_num == num :
#     print("The number you gave was Palindrome")
# else:
#     print("The number was not Palindrome")
# This was done using string slicing now i will do the same by using loops

num = int(input("Enter a number : "))
original_number = num
reverse = 0

while num > 0 :
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num//10

if reverse == original_number :
    print("The number was Palindrome")

else:
    print("The number was not Palindrome")