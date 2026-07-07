accounts = {
    "rahul" : "1234",
    "priya" : "abcd" ,
    "aman" : "pass123"
}
username = str(input("Enter a username? :"))
username = username.lower()


if username in accounts:
    password = str(input("Enter a password: "))
    if accounts[username] == password:
        print("Login successful")
    else:
        print("Inalid password or username")
else:
    print("The username does not exist")