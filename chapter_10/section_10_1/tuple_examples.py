# Chapter 10 - Tuples
# 10.1 Tuples are immutable

# File: tuple_examples.py
# Description - A few basic tuple examples.
# A tuple is a sequence of values much like a list.
# The values stored in a tuple can be any type, and they are indexed by integers.
# The important difference is that tuples are immutable.

# Example 1 - Create a tuple with multiple elements
# Create a tuple named containing the elements 'a', 'b', 'c', 'd', and 'e' and save it in variable t
# t = 'a', 'b', 'c', 'd', 'e'
# Create a tuple named containing the elements 'a', 'b', 'c', 'd', and 'e' and save it in variable t
# Although it is not necessary, it is common to enclose tuples in parentheses to help us quickly
# identify tuples when we look at Python code:
t = ('a', 'b', 'c', 'd', 'e')
# Print the tuple stored in variable t to the console.
print('Example 1 - A tuple with multiple elements:', t)

# Example 2 - Create a tuple with a single element
# To create a tuple with a single element, you have to include the final comma
t1 = ('a',)
# Print the tuple stored in variable t1 to the console.
print('Example 2 - A tuple with a single element:', t1)
# Check the data type of the tuple
print('The tuple in Example 2 is of type:', type(t1))

# Example 3 - Create an empty tuple with the built-in function tuple
# Create an empty tuple and save it in variable t3
t3 = tuple()
# Print the tuple stored in variable t3 to the console.
print('Example 3 - An empty tuple created with the built-in function tuple', t3)

# Example 4 - Create a tuple with an argument with the built-in function tuple
# Create a tuple and save it in variable t4
# If the argument is a sequence (string, list, or tuple),
# the result of the call to tuple is a tuple with the elements of the sequence
# The argument of the tuple is a string which converted into a tuple of individual characters.
t4 = tuple('lupins')
# Print the tuple stored in variable t4 to the console.
print('Example 4 - A tuple created from a string argument with the built-in function tuple', t4)

# Example 5 - Using the bracket list operator to get an element from a tuple using an index
# Most list operators also work on tuples. The bracket operator indexes an element:
# Create a tuple named containing the elements 'a', 'b', 'c', 'd', and 'e' and save it in variable t5
t5 = ('a', 'b', 'c', 'd', 'e')
# Print the element with index of 0 from the tuple that is stored in variable t5
print('Example 5 - This is the tuple stored in variable t5', t5)
print('The element with index of 0 from the tuple that is stored in variable t5 is:', t5[0])

# Example 6 - Using the slice list operator to get an element from a tuple using an index
# Create a tuple named containing the elements 'a', 'b', 'c', 'd', and 'e' and save it in variable t6
t6 = ('a', 'b', 'c', 'd', 'e')
# Print the range of element with index of 1 to 3 from the tuple that is stored in variable t6
print('Example 6 - This is the tuple stored in variable t6', t6)
print('The range of elements with index of 1 to 3 from the tuple that is stored in variable t6 is:', t6[1:3])

# Example 7 - replace one tuple with another
# Create a tuple named containing the elements 'a', 'b', 'c', 'd', and 'e' and save it in variable t7
t7 = ('a', 'b', 'c', 'd', 'e')
print('Example 7 - This is the tuple stored in variable t7', t7)
# Create a new tuple by concatenating a single-element tuple ('A',)
# with a slice of the original tuple t7 (from the second element onwards).
t7 = ('A',) + t7[1:]
print('After replacing the first element in tuple t7 now it looks like this:', t7)


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
