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


# slicing 

s = "Welcome"

print(s[1:3])
print(s[:6])
print(s[4:])
print(s[1:-1])
# in and  not functions 


s1 = "Welcome"

print("come" in s1)

print("come" not in s1)


s = "hello"
for i in s:
    print(i, end="")


s = "welcome to python"

print(s.isalnum())
print("Welcome".isalpha())
print("2020".isdigit())
print("first Number".isidentifier())
print(s.islower())
print("WELCOME".isupper())
print("  \t".isspace())


# search for str 



s = "welcome to python"

print(s.endswith("thon"))

print(s.startswith("good"))

print(s.find("come"))

print(s.find("become"))

print(s.rfind("o"))

print(s.count("o"))


# list 

list1 = list() # Create an empty list
list2 = list([22, 31, 61]) # Create a list with elements 22, 31, 61
list3 = list(["tom", "jerry", "spyke"]) # Create a list with strings
list5 = list("python") # Create a list with characters p, y, t, h, o, n

l = [1,2,3,4,5]
l[1] # access second element in the list
l[0] # access first element in the list

'''
Method name 	Description
x in s   	True if element x is in sequence s, False otherwise
x not in s   	True if element x is not in sequence s, False otherwise
s1 + s2   	Concatenates two sequences s1 and s2
s * n , n * s   	n copies of sequence s concatenated
s[i]  	 ith element in sequence s.
len(s)  	Length of sequences, i.e. the number of elements ins`.
min(s)  	Smallest element in sequence s.
max(s) 	Largest element in sequence s.
sum(s)  	 Sum of all numbers in sequence s.
for loop 	 Traverses elements from left to right in a for loop.
'''


list = [11,33,44,66,788,1]
list[0:5] # this will return list starting from index 0 to index 4

list1 = [11, 22, 44, 16, 77, 98]
print(2 in list1)


list = [1,2,3,4,5]
for i in list:
    print(i, end=" ")


list1 = [ x for x in range(10) ]
list1
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


list2 = [ x + 1 for x in range(10) ]
list2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


list3 = [ x for x in range(10) if x % 2 == 0 ]
list3
[0, 2, 4, 6, 8]


list4 = [ x *2 for x in range(10) if x % 2 == 0 ]
[0, 4, 8, 12, 16]



#dict

friends = {
'tom' : '111-222-333',
'jerry' : '666-33-111'
}
friends['tom']
dictionary_name['newkey'] = 'newvalue'


del friends['tom']
friends


friends = {
 'tom' : '111-222-333',
 'jerry' : '666-33-111'
}

for key in friends:
    print(key, ":", friends[key])


    #tuple 


t1 = () # creates an empty tuple with no data

t2 = (11,22,33)

t3 = tuple([1,2,3,4,4]) # tuple from array

t4 = tuple("abc") # tuple from string

t1 = (1, 12, 55, 12, 81)
min(t1)

max(t1)

sum(t1)

len(t1)


t = (11,22,33,44,55)
for i in t:
    print(i, end=" ")


# control statement

i = 10

if i % 2 == 0:
   print("Number is even")
else:
   print("Number is odd")


if boolean-expression:
    #statements
elif boolean-expression:
   #statements
elif boolean-expression:
   #statements
elif boolean-expression:
   #statements
else:
   #statements

today = "monday"

if today == "monday":
   print("this is monday")
elif today == "tuesday":
   print("this is tuesday")
elif today == "wednesday":
   print("this is wednesday")
elif today == "thursday":
   print("this is thursday")
elif today == "friday":
   print("this is friday")
elif today == "saturday":
   print("this is saturday")
elif today == "sunday":
   print("this is sunday")
else:
   print("something else")



today = "holiday"
bank_balance = 25000
if today == "holiday":
   if bank_balance > 20000:
      print("Go for shopping")
   else:
      print("Watch TV")
else:
   print("normal working day")


#function 

def sum(start, end):
    result = 0
    for i in range(start, end + 1):
       result += i
    print(result)

sum(10, 50)