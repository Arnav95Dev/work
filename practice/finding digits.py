# Count how many digits are present in a string

chars = "abc123de45"

value = [ "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0"]

numbers = 0

for char in chars:
    if char in value:
        numbers += 1

words = len(chars) - numbers

print(f"The amount of numbers present in {chars} are : {numbers}")
print(f"The total number of words in {chars} are : {words}")