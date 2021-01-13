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