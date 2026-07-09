# In this i will create  a  program where system will guess whether a number is prime or not

n = int(input("Enter a number! : "))

for i in range(2,n-1):
    if n % i == 0:
        print("It is not a prime number!")
        break

else:
    print("It is prime number!")