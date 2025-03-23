# Chapter 10 - Tuples
# 10.2 Comparing tuples

# File: comparing_tuples.py
# Description - Sort a list of words in descending word length order.
#
#Output:
#['yonder', 'window', 'breaks', 'light', 'what', 'soft', 'but', 'in']


# Assign a string to the variable txt.
txt = 'but soft what light in yonder window breaks'
# Split the string txt into a list of words, using whitespace as the delimiter.
words = txt.split()
# Initialize an empty list called t.
t = list()
# Iterate through each word in the words list.
for word in words:
    # Append a tuple containing the length of the word and the word itself to the list t.
    t.append((len(word), word))

# Sort the list t in descending order based on the first element of each tuple (the word length).
t.sort(reverse=True)

# Initialize an empty list called res.
res = list()
# Iterate through each tuple in the sorted list t, unpacking the length and word into separate variables.
for length, word in t:
    # Append the word to the list res.
    res.append(word)

# Print the list res to the console.
print(res)

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
