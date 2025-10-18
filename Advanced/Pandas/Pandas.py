"""
install all these libraries
----------------------------
pip3 or pin install pandas
pin install pyarrow

numpy
openpyxl
pandas
pyarrow
pyjanitor
ipykernel

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
    https://www.youtube.com/watch?v=2uvysYbKdjM&t=280s
    https://github.com/KeithGalli/complete-pandas-tutorial
    https://github.com/KeithGalli/complete-pandas-tutorial/blob/master/tutorial.ipynb
    https://numpy.org/doc/stable/reference/routines.linalg.html
"""

# Import library

import pandas as pd
import numpy as np

# =============================================================================================
#                              INTRODUCTION TO DATAFRAMES
# =============================================================================================

# Data frame is the main data structure of pandaslibrary. It has tables with all features associated with it.
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], columns=["A", "B", "C"], index=["x","y","z",'zz'])
print(df.head)
df.head(2)
df.tail(2)
df.columns
df.info()
ab = pd.DataFrame()
print(df.describe())

# Read data from a csv file
coffee = pd.read_csv('./data/coffee.csv')
print(coffee.head())

# Read data from a parquet file - less space same data as csv
results = pd.read_parquet('./data/results.parquet')
print(results.head())
