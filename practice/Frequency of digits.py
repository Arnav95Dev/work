# Count the frequency of a digit in a number

def frequency(n):
    count = 0
    num = 1235223322

    while num > 0 :
        digit = num % 10
        num = num // 10

        if digit == n :
            count += 1

    return count


demand = int(input("Enter the number whose frequency you wanna find out : "))
print(frequency(demand))