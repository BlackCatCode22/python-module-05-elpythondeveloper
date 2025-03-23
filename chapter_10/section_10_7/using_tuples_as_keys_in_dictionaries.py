# Chapter 10 - Tuples
# 10.7 Using tuples as keys in dictionaries

# File: using_tuples_as_keys_in_dictionaries.py
# Description - create a telephone directory that maps from last-name, first-name pairs to telephone numbers
# Output:
# Dictionary d looks like this: {('John', 'Smith'): {'phone': '555-1234'}, ('Jane', 'Doe'): {'phone': '555-5678'}}
# Type of variable d: <class 'dict'>
# After converting the dictionary to a list of tuples it looks like this: [(('John', 'Smith'), {'phone': '555-1234'}), (('Jane', 'Doe'), {'phone': '555-5678'})]
# Type of variable t: <class 'list'>
# Smith John {'phone': '555-1234'}
# Doe Jane {'phone': '555-5678'}

# Create an empty dictionary called d.
d = {}
# syntax for dictionary assignment statement:
# directory[last,first] = number
# Add a person's information using first name and last name as the key.
d[("John", "Smith")] = {"phone": "555-1234"}
# Add another person's information.
d[("Jane", "Doe")] = {"phone": "555-5678"}
print("Dictionary d looks like this:", d)
print("Type of variable d:", type(d))
# Convert the dictionary d into a list of key-value pairs (tuples) and assign it to t.
t = list(d.items())
# Print the list t to the console.
print('After converting the dictionary to a list of tuples it looks like this:', t)
print("Type of variable t:", type(t))

# This loop traverses the keys in directory, which are tuples. It assigns the elements
# of each tuple to last and first, then prints the name and corresponding telephone number.
for last, first in d:
    # print(first, last, d[last,first])
    print(first, last, d[last, first])






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
