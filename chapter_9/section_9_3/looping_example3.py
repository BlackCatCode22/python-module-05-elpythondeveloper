# Chapter 9 - Dictionaries
# 9.3 Looping and dictionaries

# File: looping_example3.py
# Description - This program uses a dictionary as the sequence in a for statement,
#               the for loop traverses the keys of the dictionary.
#               This program uses a for loop to print each key in alphabetical order
#               and the corresponding value.
#               If we want to print the keys in alphabetical order,
#               we first make a list of the keys in the dictionary using the keys method
#               available in dictionary objects,
#               and then sort that list and loop through the sorted list.
#
# Output:
# ['chuck', 'annie', 'jan']
# annie 42
# chuck 1
# jan 100

# Initialize a dictionary called counts with key-value pairs
# representing names and their corresponding counts.
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# Create a list called lst containing all the keys from the counts dictionary.
lst = list(counts.keys())
# Print the list of keys.
print(lst)
# Sort the list of keys in ascending order.
lst.sort()
# Iterate through each key in the sorted list called lst.
for key in lst:
    # Print the current key and its associated value from the counts dictionary.
    print(key, counts[key])

# Reference:
# Python Documentation
# https://docs.python.org/3/contents.html
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









