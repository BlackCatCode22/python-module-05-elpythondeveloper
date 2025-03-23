# Chapter 9 - Dictionaries
# 9.4 Advanced text parsing

# File: count2.py
# Description - This program read through the lines of the file,
# break each line into a list of words, and then loops through each of
# the words in the line and count each word using a dictionary.
# We use the string methods lower, punctuation, and translate to handle text with punctuations.

# Import the string module which provides string-related constants and functions.
import string

# Prompts the user to enter a file name and stores it in the fname variable.
fname = input('Enter the file name: ')

#----- try except block -----
try:
    # Attempt to open the file specified by fname and assign the file handle to fhand.
    fhand = open(fname)
# If an error occurs during file opening, print an error message.
except:
    print('File cannot be opened:', fname)
    # Exit the program.
    exit()
#----- try except block -----

# Initialize an empty dictionary called counts to store word counts.
counts = dict()
# Iterate through each line in the opened file.
for line in fhand:
    # Remove trailing whitespace characters (like newline) from the line.
    line = line.rstrip()
    # Remove punctuation characters from the line.
    line = line.translate(line.maketrans("", "", string.punctuation))
    # Convert the line to lowercase.
    line = line.lower()
    # Split the line into a list of words, using whitespace as the delimiter.
    words = line.split()
    # Iterate through each word in the words list.
    for word in words:
        # Check if the word is already a key in the counts dictionary.
        if word not in counts:
            # If the word is not in the dictionary, add it as a key with a value of 1 (first occurrence).
            counts[word] = 1
        # If the word is already in the dictionary, increment its value by 1.
        else:
            counts[word] += 1

# Print the counts dictionary, which contains the word counts.
print(counts)

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
