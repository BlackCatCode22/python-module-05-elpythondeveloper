# file: ex_11_03.py
# Extracting a host name using findall and a Regular Expression - Cooler Regex Version

import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# Starting at the beginning of the line, look for the string From
y = re.findall('^From .*@([^ ]*)',lin)
print(y)