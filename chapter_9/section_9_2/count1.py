# Chapter 9 - Dictionaries
# 9.2 Dictionaries and files

# File: count1.py
# Description - This program read through the lines of the file,
# break each line into a list of words, and then loop through each of
# the words in the line and count each word using a dictionary.
#

# Prompts the user to enter a file name and stores it in the fname variable.
fname = input('Enter the file name: ')
# Attempts to open the file specified by fname and assigns the file handle to fhand.
try:
    fhand = open(fname)
# If an error occurs during file opening, prints an error message.
except:
    print('File cannot be opened:', fname)
    # Exits the program.
    exit()

# Initializes an empty dictionary called counts to store word counts.
counts = dict()
# Iterates through each line in the opened file.
for line in fhand:
    # Splits the current line into a list of words, using whitespace as the delimiter.
    words = line.split()
    # Iterates through each word in the words list.
    for word in words:
        # Checks if the word is already a key in the counts dictionary.
        if word not in counts:
            # If the word is not in the dictionary, adds it as a key with a value of 1 (first occurrence).
            counts[word] = 1
        # If the word is already in the dictionary, increments its value by 1.
        else:
            counts[word] += 1

# Prints the counts dictionary, which contains the word counts.
print(counts)

# Reference:
# built-in functions
# https://docs.python.org/3/library/functions.html
# https://docs.python.org/3/tutorial/datastructures.html
# Dictionaries
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# https://www.py4e.com/code3/count1.py
# https://www.py4e.com/code3/romeo.txt