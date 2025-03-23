# Chapter 11 - Regular expressions
# 11.3 Combining searching and extracting

# File: re10.py
# Description - Read all the lines in a text file using a regular expression.

# Search for lines that start with X
# followed by any non whitespace characters
# and ':' # followed by a space and any number.
# The number can include a decimal.
# Import the re module, which provides regular expression operations.
import re
# Open the file mbox-short.txt and assign the file handle to hand.
hand = open('mbox-short.txt')
# Iterate through each line in the opened file.
for line in hand:
    # Remove trailing whitespace characters (like newline) from the line.
    line = line.rstrip()
    # Check if the line matches the following pattern:
    # Starts with X ('^X')
    # Followed by zero or more non-whitespace characters ('\S*')
    # Followed by a colon and a space (': ')
    # Followed by one or more digits or periods ('[0-9.]+')
    # The r prefix indicates a raw string, preventing backslash escape issues.
    if re.search(r'^X\S*: [0-9.]+', line):
        # If the regular expression is found, print the line to the console.
        print(line)

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