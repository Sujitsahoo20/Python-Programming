# STRINGS
"""
In python anything that you enclose b/w single or double qoutation marks is considered a string.
A string is essentially a sequence or array of textual data.
String are used when working with Unicode characters.
"""

name = "Sujit"
friend = "Harshit"
anotherfriend = "Abhinav" # single line string

x = """Hii my name is Sujit
Currently pursuing BE-CSE
from Chandigarh University
Mohali, Punjab"""  # multiline string

print("Hello, " + name)

print(x)

print(name[0])

for charcter in name:
    print(charcter)