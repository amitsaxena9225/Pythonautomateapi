""" MetaCharacters
#Metacharacters are characters that are interpreted in a special way by a RegEx engine. Here's a list of metacharacters:

[] . ^ $ * + ? {} () \ |
"""


import re
string = 'xyz'
pattern = '[abc]'
result = re.compile(r'[abc]')
m1 = result.search('xyz')
print(m1)