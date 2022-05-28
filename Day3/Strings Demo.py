# create string variable

# to define string

str = 'Murali'
str1 = "Manohar"
#creating empty string variables
name = ''
name2 = ""

#mutable = can not change the value of variable
#immutable = can change the value of variable
#strings are immutable


# + and * with strings
name5 = "Murali"
print(name5+"Manohar")
print(str*5)

#slicing []
print(name5[1:3]) # u r
print(name5[:5])# Mural
print(name5[2:]) #rali
print(name5[2:-1])#ral


#ord() and chr()

print(ord("M"))
print(chr(72))

#min()  max()   len()

print(min('murali'))
print(max("murali"))
print(len("murali"))


# in, not operators

s = "Murali"
print("ra" in s)
print("ab" in s)

print("ra" not in s)
print("ab" not in s)
print("-------------------------")
print("Murali"=="murali")
print("Murali"<"murali")

#useful methods
str.upper()
str.lower()
str.isalnum()
str.isalpha()
str.isdigit()
str.isspace()
str.isidentifier()

# Searching for Substrings
print(str.startswith("M"))
print(str.endswith("i"))
print(str.count("a"))
print(str.find("u"))

# converting strings
s = "python"
s1 = s.capitalize()
print(s1)
print(s.title())
print(s.swapcase())
print(s.replace("M","m"))

#Reverse a string
s = "python"
rev_str =""
for i in s:
    rev_str = i+rev_str

print(rev_str)

print("-----------")
s = "PYTHON"
rev_str2 = s[::-1]
print(rev_str2)