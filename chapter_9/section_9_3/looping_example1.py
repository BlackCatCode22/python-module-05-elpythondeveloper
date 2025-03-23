# Chapter 9 - Dictionaries
# 9.3 Looping and dictionaries

# File: looping_example1.py
# Description - This program uses a dictionary as the sequence in a for statement,
#               the for loop traverses the keys of the dictionary.
#               This program uses a for loop to print each key and the corresponding value
# Output:
# chuck 1
# annie 42
# jan 100

# Initialize a dictionary called counts with key-value pairs
# representing names and their corresponding counts.
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# Iterate through each key in the counts dictionary.
for key in counts:
    # Print the current key and its associated value from the counts dictionary.
    print(key, counts[key])

# Reference:
# Python Documentation
# https://docs.python.org/3/contents.html
# The Python Tutorial
# https://docs.python.org/3/tutorial/index.html
# Data Structures
# https://docs.python.org/3/tutorial/datastructures.html
# Dictionaries
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# 4. More Control Flow Tools - 4.2 for statements
# https://docs.python.org/3/tutorial/controlflow.html#for-statements