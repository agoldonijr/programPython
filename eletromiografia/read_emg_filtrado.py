##---------------------------------------------------------------------------##
##Esse programa faz a leiteura de um arquivo csv (separado por virgular)	 ##
##referente a eletromiografia de um cão e gera o grafico referente ao que 	 ##
##foi lido
##---------------------------------------------------------------------------##

import csv
import matplotlib.pyplot as plt

#variavel global do dado
#Uma matriz de duas colulas e n linhas: 

# coluna 0 = tempo
# coluna 1 = eletromiografia
emg = []

#print do grafico para um argumento
def print_emg_graf(dado):
	x = []
	y = []
	for i in range(len(dado)):
		x.append(dado[i][0])
		y.append(dado[i][1])
	
	plt.plot(x, y, 'bo-')
	plt.xlabel('Tempo (s)')
	plt.ylabel('EMG')
	plt.show()

#print do grafico para dois argumentos
def print_graf(x,y):
	
	plt.plot(x, y, 'bo-')
	plt.xlabel('Tempo (s)')
	plt.ylabel('EMG')
	plt.show()

# Low pass filter second order
# dt = intervalo de tempo
# rc = intervalo de tempo
def low_pass_filter (dt, rc):
	filtered_t = []
	filtered_emg = []

	#a = float(dt / (rc + dt))
	a = 0.9
	filtered_t.append(emg[0][0])
	filtered_emg.append(a * float(emg[0][1]))
	
	for i in range(1, len(emg)):
		filtered_emg.append(a * filtered_emg[i-1] + a * (float(emg[i][1]) - filtered_emg[i-1]))
		filtered_t.append(emg[i][0])

	#print do grafico
	print_graf(filtered_t, filtered_emg)

#leitura do dado
def read_emg(name_file):
	for r in csv.reader(open(name_file,'r')):
  		emg.append(r)

#	for i in dado:
#		print (i) 


##---------------------------------------------------------------------------##
##							Funcao main										 ##
##---------------------------------------------------------------------------##
#nome do arquivo para leitura
name_file = input('Nome do arquivo: ').strip()
read_emg(name_file)
low_pass_filter(float(input("dt for low pass filter: ")), float(input("rc for low pass filter: ")))
print_emg_graf(emg)
