
from loguru import logger

#string indexing and slicing

user_name = "deepak Kumar"

print(user_name[0:4])
print(user_name[:7])
print(user_name[2])

#string immutablility
user_name[0]= "k"
print(user_name)
print(id(user_name))
user_name = "D" + user_name[1:] #indirect
print(id(user_name))

#string methods
new_user = "DegfPGLHL kGOHGidguP"
print(new_user.lower())
print(new_user.upper())
print(new_user.title())
print(new_user.capitalize())
print(new_user.swapcase())

#seearch and check
print(new_user.find('G')       )  # index or -1
print(new_user.find('g')       )  # index or -1
print(new_user.index('i')      )  # like find() but raises error
print(new_user.startswith('De'))  # True
print(new_user.endswith('uP') , )  # True

#Validation (Boolean)
s = "asdgag"
t = "234452"
u = "gsdg4342"
v = "  "
w = "WGQREW"
print(s.isalpha())     # letters only
print(t.isdigit())     # digits only
print(u.isalnum())     # letters + digits
print(v.isspace())     # whitespace only
print(s.islower())     # all lowercase
print(w.isupper())     # all uppercase

# Modification

s = "'My name is Tony Stark'   "
print(s.replace('a', 'x'))     # replaces 'a' with 'x'
print(s.strip())               # removes both-side spaces
print(s.lstrip(), s.rstrip())  # left/right strip
print(s.split(' '))          # split into list

words = ['Hello', 'Deeps', 'from', 'Odisha']
sentence = ' '.join(words)
print(sentence)

#fstring
name = "Deepak"
age = 24
print(f"My name is {name} and I am {age} years old.")

# format()
print("My name is {} and I am {} years old.".format(name, age))

# String Comparisons
'apple' < 'banana'   # True
'abc' == 'ABC'       # False

# Escape characters 
s = "Deeps said, \"Python is cool!\"\nLet's go!"
print(s)
print("C:\\Users\\Deepak\\Documents\\project.py")
print("Name:\tDeepak\n Age:\t24\nCity:\tCuttack ")
print("Roses are red,\n   Violets are blue\n Coding is fun,\n   And so are you.")
print("Welcome to \"Deeps' Coding World\"\nWhere ideas \ code \ learn \ repeat")