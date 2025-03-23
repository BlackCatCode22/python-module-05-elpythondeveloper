# Chapter 10 - Tuples
# 10.8 List Comprehension

# File: list_comprehension.py
# Description - Create a sequence by using data from another sequence
#               Convert a list of strings – each string storing digits – into numbers that you can sum up.
# Output:
# The list of strings called list_of_ints_in_strings looks like this:: ['42', '65', '12']
# The list of integers called list_of_ints looks like this:: [42, 65, 12]
# The sum of all integers in list list_of_ints is: 119

# Create a list of strings, each string represents an integer.
list_of_ints_in_strings = ['42', '65', '12']
# Initialize an empty list called list_of_ints to store the integer values.
list_of_ints = []
# Iterate through each string x in the list_of_ints_in_strings list.
for x in list_of_ints_in_strings:
    # Convert the string x to an integer using the int() function and append it to the list_of_ints list.
    list_of_ints.append(int(x))
# Calculate and print the sum of all integers in the list_of_ints list.
print("The list of strings called list_of_ints_in_strings looks like this::",list_of_ints_in_strings)
print("The list of integers called list_of_ints looks like this::",list_of_ints)
print("The sum of all integers in list list_of_ints is:",sum(list_of_ints))




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
