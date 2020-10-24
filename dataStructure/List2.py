x=list(range(10))
print(x)
print(x[:])
print(x[4:])
x[0:5]=[5,4,3,2]
x[0:6:2]=[5,4,3] 
print(x)
print(x[2:6])
print(x[::2])
for i in x[2:30:6]:
    print(i)