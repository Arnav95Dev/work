# in this i'm counting number of vowels and consonents in a string
str = str(input("Enter a word:"))
str = str.lower()
str = str.replace(" ","")
a = str.count("a")
e = str.count("e")
i = str.count("i")
o = str.count("o")
u = str.count("u")
vowels = a+e+i+o+u
consonents = len(str) - vowels
print(f'''
      number of a = {a}
      number of e = {e}
      number of i = {i}
      number of o = {o}
      number of u = {u}
      so , The total number of vowels in the word is = {vowels}
      And the total number of consonents in the word is = {consonents}
      ''')