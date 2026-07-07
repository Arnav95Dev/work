# Day 3 of doing DSA of Python

gate1 = ["Rahul" , "Aman" , "Priya" , "Riya"]
gate2 = ["Priya" , "Karan" , "Aman" , "Neha"]
gate3 = ["Aman" , "Riya" , "Rohit" , "Priya"]

gate1 = set(gate1)
gate2 = set(gate2)
gate3 = set(gate3)


intersection1 = gate1 & gate2
intersection2 = intersection1 & gate3

print(intersection2)

only2_1 = gate3 & gate2
only2_2 = gate2 & gate1
only2_3 = gate1 & gate3
union1 = only2_1 | only2_2 | only2_3

union2 = gate1 | gate2 | gate3
result = union2 - union1
print(result)