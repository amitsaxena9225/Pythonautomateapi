print(help(int))

Source:"http://www.pythonlake.com/int-from_bytes"


http://opensourceforgeeks.blogspot.com/2015/10/how-python-works.html

#Introduction
#Return the integer represented by the given array of bytes.

#Syntax
int.from_bytes(bytes, byteorder, *, signed=False) -> int

Parameters
byteorder must be either 'little' or 'big'.
from_bytes() argument 2 must be str, not int

Examples
The output is:
 >>> int.from_bytes(b'Python Lake', byteorder='big')
97287619261264698714188645
>>> int.from_bytes(b'Python Lake', byteorder='little')
122608595814425519419849040


#We count in base 10 by powers of 10:

  101 = 10
  102 = 10*10 =  100
  103 = 10*10*10 = 1,000
  106 = 1,000,000
Computers count by base 2:

  21 = 2
  22 = 2*2 = 4
  23 = 2*2*2 = 8
  210 = 1,024
  220 = 1,048,576
So in computer jargon, the following units are used:

Unit	Equivalent
1 kilobyte (KB)	1,024 bytes
1 megabyte (MB)	1,048,576 bytes
1 gigabyte (GB)	1,073,741,824 bytes
1 terabyte (TB)	1,099,511,627,776 bytes
1 petabyte (PB)	1,125,899,906,842,624 bytes

A module is a single file (or files) that are imported under one import and used. e.g.

import my_module
A package is a collection of modules in directories that give a package hierarchy.

from my_package.timing.danger.internets import function_of_love

Python
Indentation
Most
of
the
programming
languages
like
C, C + +, Java
use
braces
{}
to
define
a
block
of
code.Python
uses
indentation.

A
code
block(body
of
a
function, loop
etc.) starts
with indentation and ends with the first unindented line.The amount of indentation is up to you, but it must be consistent throughout that block.

Generally
four
whitespaces
are
used
for indentation and is preferred over tabs.Here is an example.

script.py
IPython
Shell


Nonlocal Variables
Nonlocal variable are used in nested function whose local scope is not defined. This means, the variable can be neither in the local nor the global scope.

Let's see an example on how a global variable is created in Python.

We use nonlocal keyword to create nonlocal variable.

ex:


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()


We can change our current file cursor (position) using the seek() method. Similarly, the tell() method returns our current position (in number of bytes).

>>> f.tell()    # get the current file position
56
>>> f.seek(0)   # bring file cursor to initial position
0
>>> print(f.read())  # read the entire file
This is my first file
This file
contains three lines
