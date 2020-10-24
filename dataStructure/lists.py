print("===========listIsMutableObject============")
x=list(range(10))
print(x)
print(x.index(3))
x[4]=77
print(x)
print(77 in x)
print(90 not in x)
print("===========forLoopList============")

for i in x:
    print(i)
print("===========insertList============")
print(x)
x.insert(2,999)
x.insert(3,999)
x.insert(4,999)
print(x)
print(77 in x)
x.append(333)
print(x)
print(x.count(999))
print("===========tupleIsImmutableObject============")
x=tuple(range(10))
print(x)
print(7 in x)
print(77 in x)
print(77 not in x)
print("===========forLoopTuple============")
#
# for i in x:
#     print(i)
#x[4]=77 #errro
print("===========listOfString============")
x=['a','b','c','t']
print(x)
for i in x:
    print(i)
print(x.index('b'))
x.extend(range(5))
print(x)