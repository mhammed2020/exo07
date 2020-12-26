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


def sum(start, end):
    result = 0
    for i in range(start, end + 1):
       result += i
    return result

s = sum(10, 50)
print(s)



global_var = 12         # a global variable

def func():
    local_var = 100     # this is local variable
    print(global_var)   # you can access global variables in side function

func()                  # calling function func()




global_var = 12         # a global variable

def func():
    local_var = 100     # this is local variable
    print(global_var)   # you can access global variables in side function

func()                  # calling function func()



def named_args(name, greeting):
    print(greeting + " " + name )



named_args(name='jim', greeting='Hello')

named_args(greeting='Hello', name='jim') # you can pass arguments this way too




def my_func(a, b, c):
    print(a, b, c)



def bigger(a, b):
    if a > b:
        return a, b
    else:
        return b, a

s = bigger(12, 100)
print(s)
print(type(s))


#loop

my_list = [1,2,3,4]

for i in my_list:
    print(i)


for i in range(1, 10):
    print(i)



count = 0

while count < 10:
    print(count)
    count += 1




count = 0

while count < 10:
    count += 1
    if count == 5:
         break    
    print("inside loop", count)


print("out of while loop")


count = 0

while count < 10:
    count += 1
    if count % 2 == 0:
           continue
    print(count)


#Python Generating Random numbers

import random
for i in range(0, 10):
     print(random.random())



import random
for i in range(0, 10):
   print(random.randint(1, 10))



#Python File Handling

f = open('myfile.txt', 'w')    # open file for writing
f.write('this first line\n')   # write a line to the file
f.write('this second line\n')  # write one more line to the file
f.close()                      # close the file



f = open('myfile.txt', 'r')
f.read() # read entire content of file at once
"this first line\nthis second line\n"
f.close()



f = open('myfile.txt', 'r')
f.readlines() # read entire content of file at once
["this first line\n", "this second line\n"]
f.close()

f = open('myfile.txt', 'r')
f.readline() # read the first line
"this first line\n"
f.close()



f = open('myfile.txt', 'a')
f.write("this is third line\n")
f.close()



f = open('myfile.txt', 'r')
for line in f:
   print(line)



f.close()


import pickle
f = open('pick.dat', 'wb')
pickle.dump(11, f)
pickle.dump("this is a line", f)
pickle.dump([1, 2, 3, 4], f)
f.close()


#OOP

class Person:
    
       # constructor or initializer
    def __init__(self, name): 
        self.name = name # name is data field also commonly known as instance variables

    # method which returns a string
    def whoami(self):
        return "You are " + self.name


p1 = Person('tom') # now we have created a new person object p1
print(p1.whoami())
print(p1.name)


class BankAccount:
    
     # constructor or initializer
    def __init__(self, name, money):
         self.__name = name
         self.__balance = money   # __balance is private now, so it is only accessible inside the class

    def deposit(self, money):
         self.__balance += money

    def withdraw(self, money):
         if self.__balance > money :
             self.__balance -= money
             return money
         else:
             return "Insufficient funds"

    def checkbalance(self):
         return self.__balance

b1 = BankAccount('tim', 400)
print(b1.withdraw(500))
b1.deposit(500)
print(b1.checkbalance())
print(b1.withdraw(800))
print(b1.checkbalance())


#Python Operator Overloading


import math

class Circle:

    def __init__(self, radius):
        self.__radius = radius

    def setRadius(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def __add__(self, another_circle):
        return Circle( self.__radius + another_circle.__radius )

c1 = Circle(4)
print(c1.getRadius())

c2 = Circle(5)
print(c2.getRadius())

c3 = c1 + c2 # This became possible because we have overloaded + operator by adding a    method named __add__
print(c3.getRadius())






import math
 
class Circle:
 
    def __init__(self, radius):
        self.__radius = radius
 
    def setRadius(self, radius):
        self.__radius = radius
 
    def getRadius(self):
        return self.__radius



import math

class Circle:

    def __init__(self, radius):
        self.__radius = radius

    def setRadius(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def __add__(self, another_circle):
        return Circle( self.__radius + another_circle.__radius )

    def __gt__(self, another_circle):
        return self.__radius > another_circle.__radius

    def __lt__(self, another_circle):
        return self.__radius < another_circle.__radius

    def __str__(self):
        return "Circle with radius " + str(self.__radius)

c1 = Circle(4)
print(c1.getRadius())

c2 = Circle(5)
print(c2.getRadius())

c3 = c1 + c2
print(c3.getRadius())

print( c3 > c2) # Became possible because we have added __gt__ method

print( c1 < c2) # Became possible because we have added __lt__ method

print(c3) # Became possible because we have added __str__ method

#inheritance

class Vehicle:
    
    def __init__(self, name, color):
        self.__name = name      # __name is private to Vehicle class
        self.__color = color

    def getColor(self):         # getColor() function is accessible to class Car
        return self.__color

    def setColor(self, color):  # setColor is accessible outside the class
        self.__color = color

    def getName(self):          # getName() is accessible outside the class
        return self.__name

class Car(Vehicle):

    def __init__(self, name, color, model):
        # call parent constructor to set name and color  
        super().__init__(name, color)       
        self.__model = model

    def getDescription(self):
        return self.getName() + self.__model + " in " + self.getColor() + " color"

# in method getDescrition we are able to call getName(), getColor() because they are 
# accessible to child class through inheritance

c = Car("Ford Mustang", "red", "GT350")
print(c.getDescription())
print(c.getName()) # car has no method getName() but it is accessible through class Vehicle










class MySuperClass1():
    
    def method_super1(self):
        print("method_super1 method called")

class MySuperClass2():

    def method_super2(self):
        print("method_super2 method called")

class ChildClass(MySuperClass1, MySuperClass2):

    def child_method(self):
        print("child method")

c = ChildClass()
c.method_super1()
c.method_super2()




class A():
    
    def __init__(self):
        self.__x = 1

    def m1(self):
        print("m1 from A")


class B(A):

    def __init__(self):
        self.__y = 1

    def m1(self):
        print("m1 from B")

c = B()
c.m1()


isinstance(1, int)
# True

isinstance(1.2, int)
# False

isinstance([1,2,3,4], list)
# True
 


 # exception handeling

 
try:
    f = open('somefile.txt', 'r')
    print(f.read())
    f.close()
except IOError:
    print('file not found')




try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
    result = num1 / num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like this 1, 2")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")


def enterage(age):
    if age < 0:
        raise ValueError("Only positive integers are allowed")

    if age % 2 == 0:
        print("age is even")
    else:
        print("age is odd")

try:
    num = int(input("Enter your age: "))
    enterage(num)

except ValueError:
    print("Only positive integers are allowed")
except:
    print("something is wrong")



try:
    number = eval(input("Enter a number: "))
    print("The number entered is", number)
except NameError as ex:
    print("Exception:", ex)


class NegativeAgeException(RuntimeError):
    def __init__(self, age):
        super().__init__()
        self.age = age