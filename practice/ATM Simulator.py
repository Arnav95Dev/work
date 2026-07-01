print("Do you want to check your balance or withdraw money?")
balance = int(input("Enter your current balance: "))
withdrawal = int(input("Enter the amount you want to withdraw: "))

if withdrawal > balance :
    print("Insfficient balance......")
else :
    amount = balance - withdrawal
    print(f"Your remaining balance is: {amount}")