# In this I will code a program to count number of digits in an integer using loops

n = int(input("Enter a number : "))

count = 0
 
while (n > 0):
    n = n // 10 
    count += 1

print(count)