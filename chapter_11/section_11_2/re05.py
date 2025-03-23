# Chapter 11 - Regular expressions
# 11.2 Extracting data using regular expressions

# File: re05.py
# Description - Uses findall() to find all email addresses in a string
#               and extract the email addresses from the string and save then in a string list
#               then display the string list to the console.
# Output:
# ['csev@umich.edu', 'cwen@iupui.edu']

# If we want to extract data from a string in Python we can use the findall()
# method to extract all of the substrings which match a regular expression.

# Import the re module, which provides regular expression operations.
import re
# save a string in variable s
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# Find all occurrences of one or more non-whitespace characters (\S+)
# followed by an @ symbol,
# followed by one or more non-whitespace characters \S+.
# Store the results in the list called lst.
lst = re.findall(r'\S+@\S+', s)
# print the list lst to the console.
print(lst)




# Reference:
# Python Documentation
# https://docs.python.org/3/contents.html
# built-in functions
# https://docs.python.org/3/library/functions.html
#m Built-in Types
# https://docs.python.org/3/library/stdtypes.html
# The Python Tutorial
# https://docs.python.org/3/tutorial/index.html
# 4. More Control Flow Tools - 4.1. if Statements
# https://docs.python.org/3/tutorial/controlflow.html#if-statements
# 4. More Control Flow Tools - 4.2 for statements
# https://docs.python.org/3/tutorial/controlflow.html#for-statements
# 5. Data Structures
# https://docs.python.org/3/tutorial/datastructures.html
# 5. Data Structures - 5.1 More on Lists
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
# 5. Data Structures - 5.3 Tuples and Sequences
# https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
# 5. Data Structures - 5.5 Dictionaries
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# String Methods
# https://docs.python.org/3/library/stdtypes.html#string-methods
# str.lower()
# Returns a copy of the string with all the cased characters [4] converted to lowercase.
# str.translate(table)
# Returns a copy of the string in which each character has been mapped through the given translation table.
# string — Common string operations
# https://docs.python.org/3/library/string.html
# string.punctuation
# String of ASCII characters which are considered punctuation characters in the C locale
# 8. Errors and Exceptions
# https://docs.python.org/3/tutorial/errors.html
# Regular Expressions
# https://docs.python.org/3/library/re.html
# https://en.wikipedia.org/wiki/Regular_expression
# http://www.py4e.com/code3/re01.py