# Chapter 9 - Dictionaries
# 9.1 Dictionary as a set of counters

# File: dictionary_as_a_set_of_counters_using_get.py
# Description - This program searches through a string and counts how many times each letter appears in the string
#               using the get function.
#               The count is stored in a dictionary and the dictionary is printed to the console.
#
# save a string in variable word
word = 'brontosaurus'
# Use the built-in function dict to create a new dictionary with no items and save it in variable d
d = dict()
# ----- for loop -----
# Iterate through each character c in the string  saved in variable word.
for c in word:
    # Dictionaries have a method called get that takes a key and a default value.
    # If the key appears in the dictionary, get returns the corresponding value
    # otherwise it returns the default value.
    # Get the current count of character c from dictionary d,
    # or 0 if it doesn't exist, and increment it by 1.
    d[c] = d.get(c,0) + 1
# ----- for loop -----
# Print the dictionary saved in variable d, which now contains the character counts.
print(d)


# Reference:
# built-in functions
# https://docs.python.org/3/library/functions.html
# https://docs.python.org/3/tutorial/datastructures.html
# Dictionaries
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries