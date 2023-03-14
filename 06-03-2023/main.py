import numpy as np 
import time

myArray = np.array(2)
print(myArray)

array1D = np.array([1,2,3])
print(array1D)

array2D = np.array([1,2,3], [3,2,1])
print(array2D)
array2D2 = np.array([[1,2,3], [3,2,1]])
print(array2D2)

print(array2D +  array2D2)
print(array1D.shape) #devulve una tupla

startTime = time.time()
sumNumpy=array1D+array2D
endTime = time.time() - startTime
print("numpy sum: ", endTime)

startTime1 = time.time()
for i in range(array1D.shape[0]):
    for j in range(array2D.shape[1]):
        print(array1D[i,j]+array2D[i,j])

endTime1 = time.time() - startTime1
print("for sum: ", endTime1)


"""
for i in array1D:
    for j in i:
"""