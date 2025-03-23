# Chapter 9 - Dictionaries
#
# Reference:
# built-in functions
# https://docs.python.org/3/library/functions.html
# https://docs.python.org/3/tutorial/datastructures.html
# Dictionaries
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Use the built-in function dict to create a new dictionary with no items
eng2sp = dict()
# print the dictionary with no items that is saved in variable called eng2sp
print(eng2sp)
# Add an item to the empty dictionary saved in variable eng2sp
eng2sp['one'] = 'uno'
# print the dictionary
# the order of items in a dictionary is unpredictable.
print(eng2sp)
# Add three items to the dictionary saved in variable eng2sp
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# use the len built-in function to get the number of key-value pairs in the dictionary saved in eng2sp
print(len(eng2sp))
