import sys

# Criando um objeto do tipo file
temp = open('temp.txt', 'w')

for i in range(100):
		temp.write('%03d\n' % i)

# Fechando
temp.close()

temp = open('temp.txt')

# escrevendo no terminal
for x in temp:
	# utiliznado a saida padrao do terminal
	sys.stdout.write(x)

temp.close()