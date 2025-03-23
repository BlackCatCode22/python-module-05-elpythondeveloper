# Chapter 10 - Tuples
# 10.2 Comparing tuples

# File: comparing_tuples.py

# Example 1 - Compare two tuples, (0, 1, 2) and (0, 3, 4), using the less-than operator <.
# ----- Comparison 1 -----
# It starts by comparing the first elements of both tuples: 0 and 0.
# Since 0 is equal to 0, the comparison moves to the next elements.
# ----- Comparison 2 -----
# It then compares the second elements: 1 and 3.
# Here, 1 is less than 3.
# As soon as Python finds an element in the first tuple that is less
# than the corresponding element in the second tuple, it determines
# that the first tuple is less than the second tuple, and it returns True.
print((0, 1, 2) < (0, 3, 4))

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
