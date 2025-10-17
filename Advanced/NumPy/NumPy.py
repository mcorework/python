# Import libraries for Num Py
import numpy as np

#######################################     BASICS     ########################################
a = np.array([1,2,3], dtype='int32')
print(a)
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0],[4.0,1.0,3.0]])
print(b)


# https://github.com/KeithGalli/NumPy/blob/master/NumPy%20Tutorial.ipynb
# How to get the dimension of the Array
print (b.ndim)

# Get Shape
print (b.shape)

# Get data type of the object
print (a.dtype)

# Get Size
print (a.nbytes)
print (b.itemsize)


################# ACCESSING/CHANGING SPECIFIC ELEMENTS, ROWS, COLUMNS #######################
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

# Get a specific element [r, c]
print(a[0, 5])

# Get a specific row 
print(a[1 :])

# Get a specific column
print(a[:, 2])

# Getting a little more fancy [startindex:endindex:stepsize]
print (a[0, 1:4:2])
a[1,5] = 20
a[:,2] = [13,17]
print(a)

# 3D example
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
b[:,1,:] = [[11,12], [13,15]]
print(b)
print(b[0,1,0])

################# INITIALIZING DIFFERENT TYPES OF ARRAYS #######################
# All 0s matrix
np.zeros((2,3))
# All 1s matrix
np.ones((4,2,2), dtype='int32')
# Any other number
np.full((2,2), 99)
# Any other number (full_like)
np.full_like(a, 4)
# Random decimal numbers
np.random.rand(4,2)

# Initialize and Draw a 5X5 array 
arr1 = np.ones((5,5))
arr2 = np.zeros((3,3), dtype='int16')
arr1[1:4, 1:4] = arr2
arr1[2,2] = 9
print(arr1)

# Initialize and Draw a 5X5 array 
arr1 = np.ones((5,5))
arr2 = np.zeros((3,3), dtype='int16')
arr1[1:4, 1:4] = arr2
arr1[2,2] = 9
print(arr1)

# Copying Array
a = np.array([20,30,40])
b = a.copy() # Just copies the content not the reference
a[1] = 90
print(b)


################# MATHEMATICS #######################
a = np.array([1,2,3,4])
a+2
a-2
a+=2
a/2
a*2
b = np.array([1,0,1,0])
a + b
# Take the sin
np.cos(a)