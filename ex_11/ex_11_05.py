# file: ex_11_05.py
# Escape Character example
# This code uses a regular expression to find and extract a dollar amount
# (a dollar sign followed by one or more digits or decimal points) from a given string.
# It then prints the extracted amount as a list.

import re
x = 'We just received $10.00 for cookies.'
#y = re.findall('\$[0-9.]+' ,x)
# r' makes it a raw string
y = re.findall(r'\$[0-9.]+', x)
print(y)
print(type(y))