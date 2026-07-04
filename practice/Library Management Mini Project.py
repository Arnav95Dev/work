books = {"python" , "html" , "css" , "javascript" , "c++"}

book = str(input("Enter a book name: "))

if book in books :
    print("Book issued successfully!")
    books.remove(book)
    issue = set()
    issue.add(book)
else:
    print("Book is not available")

print(f"The avilable books are : {books}")

print("Your issued books !")

print(f"Your issued books {issue}")