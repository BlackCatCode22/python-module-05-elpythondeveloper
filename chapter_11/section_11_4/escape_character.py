# Chapter 11 - Regular expressions
# 11.4 Escape character

# File: escape_character.py
# Description - Indicate that we want to simply match a character by prefixing that character
#               with a backslash. Find money amounts with a regular expression.

# Import the re module, which provides regular expression operations.
import re
# Save a string in variable x.
x = 'We just received $10.00 for cookies.'
# y = re.findall('\$[0-9.]+',x)
# The r before the string makes it a raw string.
# \$ is treated as a literal dollar sign followed by [0-9.]+.
# Find all occurrences that match the following pattern:
# A literal dollar sign ('\$')
# Followed by one or more digits or periods ('[0-9.]+')
# Store the results (the matched dollar amounts) in the list 'y'.
y = re.findall(r'\$[0-9.]+', x)

print("Variable x contains this string:",x)
print("Variable y contains this list with one element:",y)
print(type(y))
print("Now we access the first element of list y and display it, it is this string:",y[0])
print(type(y[0]))

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