# Chapter 11 - Regular expressions
# 11.3 Combining searching and extracting

# File: re13.py
# Description - Read all the lines in a text file using a regular expression.
#               Search for lines that start with From and a character
#               followed by a two digit number between 00 and 99 followed by :
#               Then print the number if one is found.

# Import the re module, which provides regular expression operations.
import re
# Open the file mbox-short.txt and assign the file handle to hand.
hand = open('mbox-short.txt')
# Iterate through each line in the opened file.
for line in hand:
    # Remove trailing whitespace characters (like newline) from the line.
    line = line.rstrip()
    # Find all occurrences that match the following pattern and capture the hour in a group:
    # Starts with 'From ' ('^From ')
    # Followed by any characters ('.*')
    # Followed by a space and two digits (' ([0-9][0-9])')
    # - The parentheses create a capturing group, capturing the hour.
    # Followed by a colon (':')
    # Store the captured group(s) (hours) in the list x.
    x = re.findall('^From .* ([0-9][0-9]):', line)
    # Check if the length of the list x is greater than 0,
    # meaning at least one match was found.
    if len(x) > 0:
        # If matches were found, print the list x to the console
        # (which will contain the captured hours).
        print(x)

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