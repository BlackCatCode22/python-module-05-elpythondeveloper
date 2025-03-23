# file: ex_11_04.py
# Extracting a host name using findall and a Regular Expression - Cooler Regex Version
# This program reads a file named mbox-short.txt,
# extracts the numerical values following the "X-DSPAM-Confidence:" lines using regular expressions,
# converts those values to floats, stores them in a list,
# and then prints the maximum value found in that list.

import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))