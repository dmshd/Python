# -*- coding: utf-8 -*-
# From the Python 'start here' tutorial
# Daniel Muyshond - 09/2020

a, b = 0, 1 # It's an abbreviation to write tuples.

while a < 10:
    # The keyword argument _end_ can be used to avoid 
    # the newline after the output, or end the output 
    # with a different string:
    print(a, end=',')
    a, b = b, a+b

