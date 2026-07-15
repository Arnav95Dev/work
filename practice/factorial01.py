# Write a function named factorial(n) that returns the factorial of a number 

def factorial(n):
    fac = 1
    for i in range(1 , n + 1):
      fac *= i
    return fac

num = int(input("Enter a number : "))

print(factorial(num))