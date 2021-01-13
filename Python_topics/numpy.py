#finding the size of each item in the array  
import numpy as np  
a = np.array([[1,2,3]])  
print("Each item contains",a.itemsize,"bytes")  





import numpy as np  
a = np.array([[1,2,3,4,5,6,7]])  
print("Array Size:",a.size)  
print("Shape:",a.shape)  



import numpy as np  
a = np.array([[1,2],[3,4],[5,6]])  
print(a[0,1])  
print(a[2,0])  



import numpy as np  
a=np.linspace(5,15,10) #prints 10 values which are evenly spaced over the given interval 5-15  
print(a)  


import numpy as np  
a = np.array([1,2,3,10,15,4])  
print("The array:",a)  
print("The maximum element:",a.max())  
print("The minimum element:",a.min())  
print("The sum of the elements:",a.sum())  


import numpy as np  
a = np.array([[1,2,30],[10,15,4]])  
print("The array:",a)  
print("The maximum elements of columns:",a.max(axis = 0))   
print("The minimum element of rows",a.min(axis = 1))  
print("The sum of all rows",a.sum(axis = 1))  