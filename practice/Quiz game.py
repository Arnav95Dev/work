# Lets make a quiz game 
a = str(input("What is the capital of India? : "))
a = a.lower()
a = a.replace(" ","")
score = 0

if a == "newdelhi" :
 print("Your answer is absolutely correct!\nYou receive a point!")
 score += 1
else:
 print("Better luck next time!")

b = str(input("What is the capital of France?: "))
b = b.lower()
b = b.replace(" ","")

if b == "paris":
 print("Damn you are way too smart")
 score += 1
else:
 print("You need to work hard on your knowledge")

print(f"Your final score is :{score}/2 ")