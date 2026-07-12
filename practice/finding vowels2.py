word = str(input("Enter a word : "))
word = word.lower()

count = 0
vowels = ["a" , "e" , "i" , "o" , "u"]

for letter in word :
    if letter in vowels:
        count += 1

else:
   print(count)    