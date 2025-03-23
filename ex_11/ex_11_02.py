# file: ex_11_02.py
# Extracting a host name using findall and a Regular Expression

import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# Look through the string until you find an at sign
y = re.findall('@([^ ]*)',lin)
print(y)