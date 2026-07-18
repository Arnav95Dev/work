# Count words in a sentence 

def count(n):
    space = 0
    n = str(n).lower()

    for word in n:
        if word in [" "]:
            space += 1
        

    return space + 1

sentence = str(input("Enter a complete sentence: "))

print(f"No. of words in this sentence is: {count(sentence)}")