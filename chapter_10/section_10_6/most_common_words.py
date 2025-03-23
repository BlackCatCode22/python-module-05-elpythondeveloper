# Chapter 10 - Tuples
# 10.6 The most common words

# File: most_common_words.py
# Description - prints the ten most common words found in the text file romeo-full.txt
# Output:
# 61 i
# 42 and
# 40 romeo
# 34 to
# 34 the
# 32 thou
# 32 juliet
# 30 that
# 29 my
# 24 thee

# Import the string module, which provides string-related constants and functions.
import string
# Open the file romeo-full.txt and assign the file handle to fhand.
fhand = open('romeo-full.txt')
# Initialize an empty dictionary called counts to store word counts.
counts = dict()
# Iterate through each line in the opened file.
for line in fhand:
    # Remove punctuation characters from the line.
    line = line.translate(str.maketrans('', '', string.punctuation))
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
        else:
            # If the word is already in the dictionary, increment its value by 1.
            counts[word] += 1

# Sort the dictionary by value
# Create an empty list called lst to store value-key pairs.
lst = list()
# Iterate through the key-value pairs of the counts dictionary.
for key, val in list(counts.items()):
    # Append a tuple containing the value and key (reversed order) to the list lst.
    lst.append((val, key))
# Sort the list lst in descending order based on the values (the first element of each tuple).
lst.sort(reverse=True)
# Iterate through the first 10 elements of the sorted list lst.
for key, val in lst[:10]:
    # Print the value followed by the key for each of the top 10 value-key pairs.
    print(key, val)



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
