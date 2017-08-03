import csv
import matplotlib.pyplot as plt

#variavel global do dado
dado = []

#print do grafico
def print_graf():
	x = []
	y = []
	for i in range(len(dado)):
		x.append(dado[i][0])
		y.append(dado[i][1])
	plt.plot(x, y, 'bo-')
	plt.ylabel('EMG')
	plt.xlabel('Tempo (s)')
	plt.show()

#leitura do dado
def read_emg(name_file):
	for r in csv.reader(open(name_file,'r')):
  		dado.append(r)

	for i in dado:
		print (i) 


##---------------------------------------------------------------------------##
##							Funcao main										 ##
##---------------------------------------------------------------------------##
#nome do arquivo para leitura
name_file = input('Nome do arquivo: ').strip()
read_emg(name_file)
print_graf()
