# let us make a password checker
passw = input("Enter a password of 8 numbers (must include @ or #): ")

P = passw.lower()
P = P.replace(" ","")
A = P.find("@")
B = P.find("#")

if A != -1 or B != -1 :
    print("Your password is strong!")
else:
   print("Your password is not that much strong(reload the site and\ntry to make a better one)")

if len(P) == 8 :
    print("You have successfully created a strong password")
    print(f"Your password XXXXXX{passw[7:9]} is saved :)")
elif len(P) > 8 :
    print("Your password is way too long")
else :
    print("Your password is way too short")