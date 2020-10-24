x={'name':"jeddou",'email':"dgmn@gmail.com",'city':"casa"}
print(x)
print("name" in x)
print("country" in x)
print(x.get("country"),"morocco") #default value in dictionnary
#simple loop
for i in x:
    print(i)
#loop with key and value
for i,k in x.items() :
    print(i,k)
print("=============indexing===========")
print(x["name"])
print("=============popMethod===========")
x={'name':"jeddou",'email':"dgmn@gmail.com",'city':"casa"}
print(x)
x.pop("email")
print(x)
print("=============del Method===========")
x={'name':"jeddou",'email':"dgmn@gmail.com",'city':"casa"}
print(x)
del x["email"]
print(x)
