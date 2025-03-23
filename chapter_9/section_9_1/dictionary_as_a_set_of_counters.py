# Chapter 9 - Dictionaries
# 9.1 Dictionary as a set of counters

# File: dictionaries_as_a_set_of_counters.py
# Description - This program searches through a string and counts how many times each letter appears in the string.
#               The count is stored in a dictionary and the dictionary is printed to the console.
#
# save a string in variable word
word = 'brontosaurus'
# Use the built-in function dict to create a new dictionary with no items and save it in variable d
d = dict()
# ----- for loop -----
# Iterate through each character c in the string  saved in variable word.
for c in word:
    # Check if the character c is not already a key in the dictionary d.
    if c not in d:
        # If c is not in d, add it as a key with a value of 1 (first occurrence).
        d[c] = 1
    else:
        # If c is already a key in d do this stuff.
        # Increment the value associated with the key c by 1.
        d[c] = d[c] + 1
# ----- for loop -----
# Print the dictionary saved in variable d, which now contains the character counts.
print(d)

# Reference:
# built-in functions
# https://docs.python.org/3/library/functions.html
# https://docs.python.org/3/tutorial/datastructures.html
# Dictionaries
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries