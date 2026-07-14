# To find the factorial of a number
num = int(input("Enter a number to find it's factorial value : "))

ans = 1

for i in range(1, num + 1):
    ans *= i

print(ans)