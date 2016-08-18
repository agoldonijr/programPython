#!/bin/python3


def fib(n):
	a,b = 0,1
	while(a<n):
		print (a, end=' ')
		a,b = b, a+b
	print()
#fib(2000)


def ask_ok (prompt, retries=4, reminder='Try againg'):
	while True:
		ok = input(prompt)
		if ok in ('y', 'yes')
