x=(11,22,33,55) #tuple immutable object
print(x[1])
print(max(x))
print(min(x))
print(len(x)) # len=size

x=[22,33,44,99,10]#list
print(x[1])
print(max(x))
print(min(x))
print(len(x))
x=range(10)#range
print("===========range============")
print(x[1])
print(max(x))
print(min(x))
print(len(x))
print("===========rangeToList============")
x=list(range(10))
print(x)
print(max(x))
print("===========rangeToTuple============")
x=tuple(range(10))
print(x)
print(min(x))
print("===========rangeToTuple============")
x=tuple(range(10))
for i in x:
    print(i)

print(min(x))
x=(11,22,33,55) #tuple
print(x[-1])
x=[22,33,44,99,10]#list mutable object
print(x[-1])
x=[1] #list with one value
x=(1,) #tuple with one value
print(x[0])
x=(1) # integer value in python3
