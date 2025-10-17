# Import libraries for Num Py
import numpy as np

#######################################     BASICS     ########################################
a = np.array([1,2,3], dtype='int32')
print(a)
b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0],[4.0,1.0,3.0]])
print(b)


# https://www.youtube.com/watch?v=QUT1VHiLmmI&t=1041s (Youtube Video)
# https://github.com/KeithGalli/NumPy/blob/master/NumPy%20Tutorial.ipynb (Github for NumPy)
# https://numpy.org/doc/stable/reference/routines.math.html  (Math Library)
# https://numpy.org/doc/stable/reference/routines.linalg.html  (Linear Algebra Library)

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

################# LINEAR ALGEBRA #######################
a = np.full((6,8),1)
a = np.ones((2,3))
b = np.full((3,2), 8) 
c = np.matmul(a,b)
print (c)

# Find the determinant
c = np.identity(3)
np.linalg.det(c)

# Determinant
# Trace
# Singular Vector Decomposition
# Eigenvalues
# Matrix Norm
# Inverse
# Etc...


################# STATISTICS #######################
stats = np.array([[1,2,3000],[4,134,6]])
print(np.max(stats, axis=1))
print(np.sum(stats))



################# REORGANIZING ARRAYS #######################
before = np.array([[1,2,3,4],[5,6,7,8]])
after =before.reshape((4,2))
print(after)

# Vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack([v1,v2,v1,v2]))

# Horizontal  stack
h1 = np.ones((2,4))
h2 = np.zeros((2,2))
np.hstack((h1,h2))

################# MISCELLANEOUS #######################
# Load Data from File
filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32').copy()
print(filedata)
print("printing the axis 0 ------ ",np.any(filedata > 90, axis=0))
print("printing the axis >50 & <90 ------ ",((filedata > 50) & (filedata <90)))

# Boolean Masking and Advanced Indexing
print(filedata > 50)
print(filedata[filedata > 50])

# You can index with a list in NumPy
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[3,5,7]])
