print("------------set like a dic but witout key----")
x={"jeddou","dgmn@gmail.com","casa","maroc","enginner"}
x1={"jeddou","dgmn@gmail.com"}
x2={"jeddou","dgmn@gmail.com","casa"}
print(x)
print(x1)
print(x2)
print(x1.issubset(x))
print(x.issuperset(x1))
print(x1.issuperset(x2))
y=x.union(x1)
print(y)
# for i in x :
#     print(i)
x=set("jeddou dgmn@gmail.com casa")
