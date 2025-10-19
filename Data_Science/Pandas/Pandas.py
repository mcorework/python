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
df.nunique()
ab = pd.DataFrame()
print(df.describe())

# =============================================================================================
#                              Loading in Dataframes from Files
# =============================================================================================

# Read data from a parquet file - less space same data as csv
results = pd.read_parquet('./data/results.parquet')
print(results.head())

## To read an excel spreadsheet
olympics_data = pd.read_excel('./data/olympics-data.xlsx', sheet_name="results")
print(olympics_data)

# Read data from a csv file
coffee = pd.read_csv('./data/coffee.csv')

# =============================================================================================
#                              Accessing Data with Pandas
# =============================================================================================

print(coffee.head()) # access first 5 rows
print(coffee.head(7)) # access first 50 rows
#coffee.loc[#Rows, #Columns]
print(coffee.loc[0])
coffee.loc[[0,1,2]]
coffee.loc[5:]
print(coffee.loc[5:8, ["Day", "Units Sold"]])
print(coffee.iloc[:, [1,2]]) #iloc uses only index values

# Setting Values
coffee.loc[1:3, "Units Sold"] = 10

# Optimized way to get single values (.at & .iat)
coffee.at[0,"Units Sold"]
coffee.iat[3,1]
coffee.Day
coffee["Day"]

# Sort Values
print(coffee.sort_values("Units Sold",ascending=False))
coffee.sort_values(["Units Sold", "Coffee Type"], ascending=[0,1])

# Iterate over dataframe with for loop
for index, row in coffee.iterrows():
    print(index)
    print(row)
    print("Coffee Type of Row:", row["Coffee Type"])
    print("\n")

# =============================================================================================
#                              Filtering Data
# =============================================================================================    

bios = pd.read_csv('./data/bios.csv')
print(bios.head())
print(bios.loc[bios["height_cm"] > 215, ["name", "height_cm"]])
bios[bios['height_cm'] > 215][["name","height_cm"]]
bios[(bios['height_cm'] > 215) & (bios['born_country']=='USA')]
bios[bios['name'].str.contains("keith", case=False)]

# Regex syntax
bios[bios['name'].str.contains('keith|patrick', case=False)]
# Other cool regex filters

# Find athletes born in cities that start with a vowel:
vowel_cities = bios[bios['born_city'].str.contains(r'^[AEIOUaeiou]', na=False)]

# Find athletes with names that contain exactly two vowels:
two_vowels = bios[bios['name'].str.contains(r'^[^AEIOUaeiou]*[AEIOUaeiou][^AEIOUaeiou]*[AEIOUaeiou][^AEIOUaeiou]*$', na=False)]

# Find athletes with names that have repeated consecutive letters (e.g., "Aaron", "Emmett"):
repeated_letters = bios[bios['name'].str.contains(r'(.)\1', na=False)]

# Find athletes with names ending in 'son' or 'sen':
son_sen_names = bios[bios['name'].str.contains(r'son$|sen$', case=False, na=False)]

# Find athletes born in a year starting with '19':
born_19xx = bios[bios['born_date'].str.contains(r'^19', na=False)]

# Find athletes with names that do not contain any vowels:
no_vowels = bios[bios['name'].str.contains(r'^[^AEIOUaeiou]*$', na=False)]

# Find athletes whose names contain a hyphen or an apostrophe:
hyphen_apostrophe = bios[bios['name'].str.contains(r"[-']", na=False)]

# Find athletes with names that start and end with the same letter:
start_end_same = bios[bios['name'].str.contains(r'^(.).*\1$', na=False, case=False)]

# Find athletes with a born_city that has exactly 7 characters:
city_seven_chars = bios[bios['born_city'].str.contains(r'^.{7}$', na=False)]

# Find athletes with names containing three or more vowels:
three_or_more_vowels = bios[bios['name'].str.contains(r'([AEIOUaeiou].*){3,}', na=False)]

# Don't use regex search (exact match)
bios[bios['name'].str.contains('keith|patrick', case=False, regex=False)]

## isin method & startswith
bios[bios['born_country'].isin(["USA", "FRA", "GBR"]) & (bios['name'].str.startswith("Keith"))]

# Query functions
bios.query('born_country == "USA" and born_city == "Seattle"')

# =============================================================================================
#                              Adding / Removing Columns
# =============================================================================================  
coffee.head()
coffee['price'] = 4.99
coffee['new_price'] = np.where(coffee['Coffee Type']=='Espresso', 3.99, 5.99) 
print(coffee)
coffee.drop(columns=['price'], inplace=True)
coffee = coffee[['Day', 'Coffee Type', 'Units Sold', 'new_price']]
coffee['revenue'] = coffee['Units Sold'] * coffee['new_price']
coffee.rename(columns={'new_price': 'price'}, inplace=True)

bios_new = bios.copy()
bios_new['first_name'] = bios_new['name'].str.split(' ').str[0]
bios_new.query('first_name == "Keith"')

bios_new['born_datetime'] = pd.to_datetime(bios_new['born_date'])
bios_new['born_year'] = bios_new['born_datetime'].dt.year
bios_new[['name','born_year']]
bios_new.to_csv('./data/bios_new.csv', index=False)
bios['height_category'] = bios['height_cm'].apply(lambda x: 'Short' if x < 165 else ('Average' if x < 185 else 'Tall'))

def categorize_athlete(row):
    if row['height_cm'] < 175 and row['weight_kg'] < 70:
        return 'Lightweight'
    elif row['height_cm'] < 185 or row['weight_kg'] <= 80:
        return 'Middleweight'
    
    else:
        return 'Heavyweight'
    
bios['Category'] = bios.apply(categorize_athlete, axis=1)

# =============================================================================================
#                              Merging & Concatenating Data
# =============================================================================================  
nocs = pd.read_csv('./data/noc_regions.csv')
bios_new = pd.merge(bios, nocs, left_on='born_country', right_on='NOC', how='left')
bios_new.rename(columns={'region': 'born_country_full'}, inplace=True)
usa = bios[bios['born_country']=='USA'].copy()
gbr = bios[bios['born_country']=='GBR'].copy()
new_df = pd.concat([usa,gbr])
combined_df = pd.merge(results, bios, on='athlete_id', how='left')

# =============================================================================================
#                              Handling Null Values
# =============================================================================================  
coffee.loc[[2,3], 'Units Sold'] = np.nan
# Make sure to set this to your Units Sold column if you want these changes to stick
coffee['Units Sold'].fillna(coffee['Units Sold'].mean()) 
# coffee['Units Sold'] = coffee['Units Sold'].interpolate()
coffee['Units Sold'].interpolate()
coffee.dropna(subset=['Units Sold']) # Use inplace=True if you want to update the coffee df
coffee[coffee['Units Sold'].notna()]

# =============================================================================================
#                              Aggregating Data
# =============================================================================================  
bios['born_city'].value_counts()

