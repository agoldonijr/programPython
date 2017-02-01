import re

#Compilando a expressao regular
#usando o compile() a expressao fica compilada e pode ser usada mais de uma vez

rex = re.compile('\w+')

# Encontra todas as ocorrencias que atendam a expressao
bjork = re.compile('[Bb]j[öo]rk')

for m in ('Björk', 'björk', 'Biork', 'Bjork', 'bjork')
	print m, '->' bool(bjork.match(m))
	#match localiza a ocorrencia no inicio do string
	#para qualquer lugar, use search()

# Substituindo texto
texto = 'A próxima faixa é Stairway to Heaven'
print texto, '->', re. sub('[Ss]tairway [Tt]o [Hh]eaven','The Rover', texto)
 
# Dividindo texto
bandas = 'Tool, Porcupine Tree e NIN'
print bandas, '->', re.split(',?\s+e?\s+', bandas)

