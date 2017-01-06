

def primo(num):
	cont = 0

	if((num % 2 == 0) and (num != 2)):
		return False;
	else:
		for i in range(2, num/2):
			if(num % i == 0):
				cont +=1

		if(cont == 0):
			return True

		else:
			return False

for i in range (1, 100):
	print( i , primo(i));

