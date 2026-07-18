# Write a function that takes a string as input and returns the number of vowels


def akshar(n):
    count = 0
    n = str(n)
    n = n.lower()
    
    for letter in n:
        if letter in [ "a" , "e" , "i" , "o" , "u" ]:
            count += 1

    return count

word = input("Enter a word : ")
print(f"No. of vowels : {akshar(word)}")