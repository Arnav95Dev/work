# This is just a password checker where user will give data and password will be checked

password_manager = [1234 , 5678 , 9999 , 0000 , 1897 , 5555]

user = int(input("Guess the password ? : "))

if user in password_manager :
    print("You have successfully found the password!!")
else:
    print("Oops! Your selected password was wrong!!")