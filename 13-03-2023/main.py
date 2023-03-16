import numpy as np

#Arreglo de una dimension
myArray = np.array([1,2,3,4,5])

#slicing
print(myArray[1:])
print(myArray[:3])
print(myArray[1:3])

#slicing negativo
print(myArray[-1])


#Arreglo de dos dimensiones
myArray = np.array([[1,2,3,4,5],[6,7,8,9,10]])

#slicing
print(myArray[1][1:2])
print(myArray[1,1:2])
print(myArray[0:2,1:2])
print(myArray[0:2,1:2])

for x in np.nditer(myArray):
    print(x)


myArray2 = np.array([1,2,3,4,5])
result = np.where(myArray2 ==3)

print(result)

#print(myArray2(result[0]))

myArray3 = np.array([1,2,3,4,5])
result = np.where(myArray3 > 2)

print(result[0])
print(result[0].shape)

print(type(result))
print(type(result[0]))