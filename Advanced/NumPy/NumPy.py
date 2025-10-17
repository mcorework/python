"""
numpy_basics_demo.py
---------------------
Comprehensive demonstration of NumPy fundamentals:
- Array creation
- Indexing & slicing
- Mathematical operations
- Linear algebra
- Statistics
- Reshaping and stacking
- File I/O
- Boolean masking and advanced indexing

References:
    https://www.youtube.com/watch?v=QUT1VHiLmmI&t=1041s
    https://github.com/KeithGalli/NumPy/blob/master/NumPy%20Tutorial.ipynb
    https://numpy.org/doc/stable/reference/routines.math.html
    https://numpy.org/doc/stable/reference/routines.linalg.html
"""

# Import library
import numpy as np

# =============================================================================================
#                                         BASICS
# =============================================================================================

# 1D and 2D arrays
a = np.array([1, 2, 3], dtype='int32')
print("Array a:", a)

b = np.array([
    [9.0, 8.0, 7.0],
    [6.0, 5.0, 4.0],
    [4.0, 1.0, 3.0]
])
print("Array b:\n", b)

# Basic properties
print("Dimension of b:", b.ndim)
print("Shape of b:", b.shape)
print("Data type of a:", a.dtype)
print("Memory size of a:", a.nbytes)
print("Item size of b:", b.itemsize)

# =============================================================================================
#                        ACCESSING / CHANGING ELEMENTS, ROWS, COLUMNS
# =============================================================================================

a = np.array([
    [1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14]
])
print("\nArray a:\n", a)

# Accessing elements
print("Element [0,5]:", a[0, 5])
print("Row 1 onwards:\n", a[1:])
print("Column 2:\n", a[:, 2])

# Slicing with step size
print("Fancy slice [0,1:4:2]:", a[0, 1:4:2])

# Modifying values
a[1, 5] = 20
a[:, 2] = [13, 17]
print("Modified array a:\n", a)

# 3D array example
b = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
b[:, 1, :] = [[11, 12], [13, 15]]
print("\n3D array b:\n", b)
print("Element b[0,1,0]:", b[0, 1, 0])

# =============================================================================================
#                        INITIALIZING DIFFERENT TYPES OF ARRAYS
# =============================================================================================

print("\n--- Array Initialization Examples ---")
print("Zeros:\n", np.zeros((2, 3)))
print("Ones:\n", np.ones((4, 2, 2), dtype='int32'))
print("Full matrix (99):\n", np.full((2, 2), 99))
print("Full_like (shape of a, fill with 4):\n", np.full_like(a, 4))
print("Random decimal numbers:\n", np.random.rand(4, 2))

# Creating a 5x5 matrix with a hollow center
arr1 = np.ones((5, 5))
arr2 = np.zeros((3, 3), dtype='int16')
arr1[1:4, 1:4] = arr2
arr1[2, 2] = 9
print("\n5x5 patterned array:\n", arr1)

# Copying arrays (deep copy)
a = np.array([20, 30, 40])
b = a.copy()
a[1] = 90
print("\nOriginal a modified:", a)
print("Copied b remains:", b)

# =============================================================================================
#                                         MATHEMATICS
# =============================================================================================

a = np.array([1, 2, 3, 4])
b = np.array([1, 0, 1, 0])

print("\n--- Math Operations ---")
print("a + 2:", a + 2)
print("a - 2:", a - 2)
print("a * 2:", a * 2)
print("a / 2:", a / 2)
print("a + b:", a + b)
print("cos(a):", np.cos(a))

# =============================================================================================
#                                      LINEAR ALGEBRA
# =============================================================================================

print("\n--- Linear Algebra ---")
a = np.ones((2, 3))
b = np.full((3, 2), 8)
c = np.matmul(a, b)
print("Matrix multiplication result:\n", c)

# Determinant
c = np.identity(3)
print("Determinant of identity matrix:", np.linalg.det(c))

# =============================================================================================
#                                        STATISTICS
# =============================================================================================

print("\n--- Statistics ---")
stats = np.array([[1, 2, 3000], [4, 134, 6]])
print("Max along axis=1:", np.max(stats, axis=1))
print("Sum of all elements:", np.sum(stats))

# =============================================================================================
#                                    REORGANIZING ARRAYS
# =============================================================================================

before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
after = before.reshape((4, 2))
print("\nReshaped array:\n", after)

# Vertical stack
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
print("Vertical stack:\n", np.vstack([v1, v2, v1, v2]))

# Horizontal stack
h1 = np.ones((2, 4))
h2 = np.zeros((2, 2))
print("Horizontal stack:\n", np.hstack((h1, h2)))

# =============================================================================================
#                              MISCELLANEOUS / FILE OPERATIONS
# =============================================================================================

# Load data from file
filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32').copy()
print("\nLoaded data:\n", filedata)

# Boolean operations
print("Any > 90 along axis 0:", np.any(filedata > 90, axis=0))
print("Values > 50 and < 90:\n", (filedata > 50) & (filedata < 90))

# Boolean masking
print("Mask (filedata > 50):\n", filedata > 50)
print("Filtered values (filedata > 50):", filedata[filedata > 50])

# Advanced indexing
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Indexed elements [3,5,7]:", a[[3, 5, 7]])
