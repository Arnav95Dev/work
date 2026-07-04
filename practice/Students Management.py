coding_club = {"Rahul" , "Aman" , "Priya" , "Riya"}
robotics_club = {"Aman" , "Riya" , "Karan" , "Neha"}

print(f"Students in both clubs  : {coding_club.intersection(robotics_club)}")
print(f"Students only in coding club : {coding_club - robotics_club}")
print(f"Students only in robotics club : {robotics_club - coding_club}")
print(f"All students in this list are : {coding_club.union(robotics_club)}")

user = str(input("Enter a student's name you want to check: "))

both = coding_club.intersection(robotics_club)
only1 = coding_club - robotics_club
only2 = robotics_club - coding_club

if user in both :
    print(f"{user} is in both the clubs")
elif user in only1:
    print(f"{user} is in only coding club")
elif user in only2 :
    print(f"{user} is in only robotics club")
else:
    print(f"{user} is not in any club")