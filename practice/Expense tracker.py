food = int(input("How much amount is being spend on foods?(in rupees): "))
travel = int(input("How much amount is being spend on travels?(in rupees): "))
Gaming = int(input("How much amount is being spend on gaming?(in rupees): "))

expenses = [ food , travel , Gaming]
expenses.sort()
print(f"Highest expense : {max(expenses)} ")
print(f"Total expense : {sum(expenses)}")