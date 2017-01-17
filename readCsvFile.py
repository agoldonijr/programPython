import csv

# a rotina de leitura recebe um objeto arquivo
dt = csv.reader(file('dt.csv'))

#para cada registro do arquivo, imprima
for reg in dt:
		print reg

