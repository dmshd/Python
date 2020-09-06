# -*- coding: utf-8 -*-
# prime-numbers example from
# https://docs.python.org/3/tutorial/controlflow.html
# introduces 'break' statement

for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break
	else:
		# loop fell though without finding a factor
		print(n, 'is a prime number')
 
