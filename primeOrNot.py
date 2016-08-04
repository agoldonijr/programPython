#!/bin/python3

max = 100000

for number in range(2, max):
	for x in range(2, number):
		if number % x == 0:
		#	print(number, 'equals', x, '*', number//x)
			break
	else:
		print(number, 'is a prime number')
