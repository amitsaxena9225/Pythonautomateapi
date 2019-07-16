'''import re

line = "India is my country"

pattern ="I"

a = re.match(pattern,line)

#a = re.split(pattern,line)

print(a)

#print (a.group())

import re

line = "India Is my country"

pattern ="I"

a = re.search(pattern,line)

#a = re.split(pattern,line)

print(a)

import re

line = "India Is my country I"

pattern ="I"

a = re.findall(pattern,line)

#a = re.split(pattern,line)

print(a)

import re

line = "India Is my country I"

pattern ="I"

a = re.split(pattern,line)

#a = re.split(pattern,line)

print(a)

import re

line = "IndIa Is Iy country I"

pattern ="I"

a = re.split(pattern,line,maxsplit=6)

#a = re.split(pattern,line)

print(a)'''

import re

line = "IndIa Is Iy country I"

pattern ="I"

a = re.sub(pattern,'H',line)

#a = re.split(pattern,line)

print(a)

