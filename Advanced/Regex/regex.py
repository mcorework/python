r"""
# 🔍 Regular Expressions (RegEx) in Python — Overview

## 📘 Introduction
A **Regular Expression (RegEx)** is a **sequence of characters that defines a search pattern**.  
They are powerful tools for **searching, matching, validating, and manipulating strings** based on specific text patterns.  

Python provides the built-in **`re`** module for working with regular expressions.
---

### 3. Links
[Regex in Python - Corey Schafer](https://www.youtube.com/watch?v=K8L6KVGG-7o)

.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)

## ⚙️ Importing the `re` Module
```python
import re
""" 


import re
#=============================================================================
#🧩 Example 1 — Basic
#=============================================================================
# Note - Use raw string to avoid the escape sequence.
text_to_search = r'''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'start', re.I) #compile methods separates the patterns and assigns to a variable
matches = pattern.search(sentence)
#print(matches)


pattern = re.compile(r'\.') #searches periods
pattern = re.compile(r'coreyms\.com') #searches periods



# --------------------------------------------------------
# 🔹 Example 1 — Basic 1
# --------------------------------------------------------
# '.' is a special regex character, so escape it with '\.'
pattern = re.compile(r'\.')

# email matching
pattern = re.compile(r'coreyms\.')

# digit matching
pattern = re.compile(r'\d')

# capital letter negates (D,W,....) matching
pattern = re.compile(r'\D')

# word matching (lower case, upper case a-z A-Z 0-9)
pattern = re.compile(r'\w')

# not a word character
pattern = re.compile(r'\W')

# white space (space, tab, new line)
pattern = re.compile(r'\s')

# not white space 
pattern = re.compile(r'\S')

# --------------------------------------------------------
# 🔹 Example 2 — Literal Characters
# --------------------------------------------------------
# \b word boundary
pattern = re.compile(r'\bHa')

# \B not a word boundary
pattern = re.compile(r'\BHa')

# ^ beginning of a string
pattern = re.compile(r'^Start')

# $ ending string
pattern = re.compile(r'end$')

# --------------------------------------------------------
# 🔹 Example 3 — Phone numbers
# --------------------------------------------------------
# phone number search
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

# [] character set to match (. or - in phone numbes) the options inside the bracket
pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')

# [] character set to match (800 phone numbes)
pattern = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d')

# Adding Quantifiers
# [] character set to match (. or - in phone numbes) the options inside the bracket
pattern = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')
pattern = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')
pattern = re.compile(r'Mr')
pattern = re.compile(r'Mr\.?\s')
pattern = re.compile(r'Mr\.?\s[A-Z]')





# --------------------------------------------------------
# 🔹 Example 4 — Range of letters and numbers
# --------------------------------------------------------
# phone number search
pattern1 = re.compile(r'[1-5]')
pattern1 = re.compile(r'[a-z]')
pattern1 = re.compile(r'[a-zA-Z]') #matches any of the range of characters

pattern1 = re.compile(r'[^a-zA-Z]') #negates the search with carat character
pattern1 = re.compile(r'[^b]at') #not be followed by at - bat is excluded


# --------------------------------------------------------
# Result
# --------------------------------------------------------
matches = pattern.finditer(text_to_search)
#matches = pattern.finditer(sentence)

for match in matches:
    print(match)

with open('data.txt','r', encoding='utf-8') as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    #for match in matches:
    #    print(match)