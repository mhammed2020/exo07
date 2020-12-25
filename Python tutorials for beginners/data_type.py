x = 100                       # x is integer
pi = 3.14                     # pi is float
empname = "python is great"   # empname is string

a = b = c = 100 # this statement assign 100 to c, b and a.


print("*"*50)

x = 1   # initial value of x is 1
y = 2   # initial value of y is 2

y, x = x, y # assign y value to x and x value to y


name = input("Enter your name: ")
print(name)

age = int(input("Enter your age: "))

print(age)
print(type(age))


import math, os

print(math.pi)
print(math.e)

print(os.getcwd())


# srt
name = "tom" # a string
mychar = 'a' # a character

print(name)
print(mychar)

name1 = str() # this will create empty string object
name2 = str("newstring") # string object containing 'newstring'

print(name1)
print(name2)

str1 = "welcome"
str2 = "welcome"

print(id(str1),  id(str2))

str1 += " mike"

#str1[1]='b' error  Strings in Python are Immutable

name = "tom"

print(name[0])
print(name[1])


s = "tom and " + "jerry"
print(s)

s = "spamming is bad " * 3
print(s)
