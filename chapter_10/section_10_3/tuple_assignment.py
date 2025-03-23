# Chapter 10 - Tuples
# 10.3 Tuple assignment

# File: tuple_assignment.py

# Example 1 - Example showing how to have a tuple on the left side of an assignment statement.
#             Use a two-element list (which is a sequence) and assign the first
#             and second elements of the sequence to the variables x and y in a single statement.
# Create a list named m containing the strings have and fun.
m = [ 'have', 'fun' ]
# Unpack the elements of the list m into the variables x and y.
x, y = m
print('Example 1 - This is the list called m:', m)
# Print the value of x to the console.
print('The first element of the list saved in x has this value:', x)
# Print the value of y to the console.
print('The first element of the list saved in y has this value:', y)

# Example 2 - Showing how Python translates the tuple assignment syntax
# Create a list named m2 containing the strings have and fun.
m2 = [ 'Evanescence', 'No Doubt' ]
print('Example 2 - This is the list called m2:', m2)
# Assign the first element of the list m2 to the variable j.
j = m2[0]
# Assign the second element of the list m2 to the variable k.
k = m2[1]
# Print the value of j to the console.
print('The first element of the list saved in j has this value:', j)
# Print the value of k to the console.
print('The first element of the list saved in k has this value:', k)

# Example 3 - use a tuple on the left side of the assignment statement with parentheses
# Create a list named m3 containing the strings have and fun.
m3 = [ 'Pearl Jam', 'Soundgarden' ]
print('Example 3 - This is the list called m3:', m3)
# Unpack the elements of the list m3 into a tuple (v, w).
(v, w) = m3
# Print the value of v to the console.
print('The first element of the list saved in v has this value:', v)
# Print the value of w to the console.
print('The first element of the list saved in m has this value:', w)

# Example 4 - Swap the values of two variables in a single statement
# Create a list named m4 containing the strings have and fun.
m4 = [ 'Guns N Roses', 'Metallica' ]
print('Example 4 - This is the list called m4:', m4)
# Unpack the elements of the list m3 into a tuple (q, r).
(q, r) = m4
# Print the values to the console.
print('Before being swapped the element saved in q has this value:', q)
print('Before being swapped the element saved in r has this value:', r)
# Swap the values of q and r using simultaneous assignment.
q, r = r, q
# Print the values to the console.
print('After being swapped the element saved in q has this value:', q)
print('After being swapped the element saved in r has this value:', r)

# Example 5 - Split an email address into a user name and a domain
# The number of variables on the left and the number of values on the right must be the same.
# The right side can be any kind of sequence (string, list, or tuple).
# The return value from split is a list with two elements
# Assign the string monty@python.org to the variable addr.
addr = 'monty@python.org'
print('Example 5 - Email string saved in variable addr is:', addr)
# Split the string addr at the @ character and unpack the resulting
# two parts into the variables uname and domain.
uname, domain = addr.split('@')
# Print the value of uname to the console.
print('After splitting the email on @ character, the left side of the string is this:', uname)
# Print the value of domain to the console.
print('After splitting the email on @ character, the right side of the string is this:',domain)

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
