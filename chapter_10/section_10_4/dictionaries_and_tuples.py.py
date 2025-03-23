# Chapter 10 - Tuples
# 10.4 Dictionaries and tuples

# File: dictionaries_and_tuples.py

# Example 1 - Use a Dictionary method called items to return a list of tuples
# Create a dictionary d with key-value pairs.
d = {'a':10, 'b':1, 'c':22}
print('Example 1 - Use a Dictionary method called items to return a list of tuples')
print('The dictionary with key-value pairs saved in d looks like this:', d)
# Convert the dictionary d into a list of key-value pairs (tuples) and assign it to t.
t = list(d.items())
# Print the list t to the console.
print('After converting the dictionary to a list of tuples it looks like this:', t)

# Example 2 - Use a Dictionary method called items to return a list of tuples and sort them
# Create a dictionary d with key-value pairs.
e = {'c':22, 'b':1, 'a':10}
print('Example 2 - Use a Dictionary method called items to return a list of tuples and sort them')
print('The dictionary with key-value pairs saved in e looks like this:', e)
# Convert the dictionary d into a list of key-value pairs (tuples) and assign it to t.
x = list(e.items())
# Print the list x to the console.
print('After converting the dictionary to a list of tuples it looks like this:', x)
x.sort()
print('After sorting the list of tuples it looks like this:', x)




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
