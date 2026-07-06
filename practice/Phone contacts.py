# Let's make a program for contacts:

family_contacts = {"Vaibhav" , "Raj" , "Sita" , "Mohan" , "Sunita"}
friends_contacts = {"Rohan" , "Raj" , "Dolu" , "Sunita" , "Meeru"}

print(f"The names present both in the list: {family_contacts & friends_contacts}")
print(f"And all the contacts : {family_contacts| friends_contacts}")
print(f"Names only in family list : {family_contacts - (family_contacts&friends_contacts)}")
print(f"Names only in the friends list : {friends_contacts - (family_contacts & friends_contacts)}")
print(f"Names belong to only one set : {(family_contacts|friends_contacts) - (friends_contacts & family_contacts)}")
