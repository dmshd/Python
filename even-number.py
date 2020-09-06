# -*- coding: utf-8 -*-
# even numbers example from
# https://docs.python.org/3/tutorial/controlflow.html
# introduces 'continue' statement

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)
