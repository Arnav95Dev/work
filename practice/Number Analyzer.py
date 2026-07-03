a = int(input("Enter any desired random number: "))
b = int(input("Enter another desired random number: "))
c = int(input("Enter another desired random number: "))
d = int(input("Enter another desired random number: "))
e = int(input("Enter another desired random number: "))
f = int(input("Enter another desired random number: "))
g = int(input("Enter another desired random number: "))
h = int(input("Enter another desired random number: "))
i = int(input("Enter another desired random number: "))
j = int(input("Enter another desired random number: "))

number = [a , b , c , d , e , f , g , h , i , j]
total = a+b+c+d+e+f+g+h+i+j
number.sort()
print(f"The largest number you gave is : {number[9]}")
print(f"The smallest number you gave is : {number[0]}")
print(f"The total of your numbers are : {total}")
print(f"The average of the numbers are : {total/10}")

even = 0 
odd  = 0

if a%2 == 0 :
    even += 1
else :
   odd += 1

if b%2 == 0 :
    even += 1
else :
   odd += 1

if c%2 == 0 :
    even += 1
else :
   odd += 1

if d%2 == 0 :
    even += 1
else :
   odd += 1

if e%2 == 0 :
    even += 1
else :
   odd += 1

if f%2 == 0 :
    even += 1
else :
   odd += 1

if g%2 == 0 :
    even += 1
else :
   odd += 1

if h%2 == 0 :
    even += 1
else :
   odd += 1

if i%2 == 0 :
    even += 1
else :
   odd += 1

if j%2 == 0 :
    even += 1
else :
   odd += 1

print(f"Even numbers : {even}")
print(f"Odd numbers : {odd}")