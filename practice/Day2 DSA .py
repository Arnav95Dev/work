# Another DSA challenge for me 
# The main task is to get the numbers 5 , 7 , 8 , 10

list1 = [1 , 2 , 3 , 4 , 5 , 6 , 7]
list2 = [4 , 5 , 6 , 7 , 8 , 9 , 10]
list3 = [2 , 4 , 6 , 8 , 10]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

intersection_between_1and2 = set1 & set2
intersection_between_2and3 = set2 & set3
union = intersection_between_1and2 | intersection_between_2and3
intersection_between_1_and_3 = set1 & set3
result = union - intersection_between_1_and_3
print(result)