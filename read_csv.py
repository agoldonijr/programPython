import csv
import sys
import os.path

dado = []
cabecalho = []
option = []

def read_all(name_file):
	i = 0
	f = open(name_file, "r")
	for r in csv.reader(open('Tequila-completo.csv','rb')):
	  	if(i <= 24):
			aux = f.readline()
			cabecalho.append(aux.split(":"))
			cabecalho[i][1] = cabecalho[i][1].strip()
			cabecalho[i][2] = cabecalho[i][2].replace("Sampling frequency", "").strip()
			cabecalho[i][3] = cabecalho[i][3].replace("Number of points","").strip()
			cabecalho[i][4] = cabecalho[i][4].replace("X start","").strip()
			cabecalho[i][5] = cabecalho[i][5].replace("Unit","").strip()
			cabecalho[i][6] = cabecalho[i][6].replace("Domain Unit","").strip()
			cabecalho[i][7] = cabecalho[i][7].strip()
		elif(i>24) and (i<172):
			aux = f.readline()
			option.append(aux.split(":"))
			#option[i][1] = option[i][1].strip()
			
		else:
			aux = f.readline()
			dado.append(aux)
		i+=1
	
	print(cabecalho)
	#print(option)
	#print(dado)
			

#lendo header do arquivo
def read_reader(name_file):
	f = open(name_file, "r")

	#lendo as 24 primeiras linhas e salvando no 
	for i in range (0,24):
		aux = f.readline()
		cabecalho.append(aux.split(":"))
		cabecalho[i][1] = cabecalho[i][1].strip()
		cabecalho[i][2] = cabecalho[i][2].replace("Sampling frequency", "").strip()
		cabecalho[i][3] = cabecalho[i][3].replace("Number of points","").strip()
		cabecalho[i][4] = cabecalho[i][4].replace("X start","").strip()
		cabecalho[i][5] = cabecalho[i][5].replace("Unit","").strip()
		cabecalho[i][6] = cabecalho[i][6].replace("Domain Unit","").strip()
		cabecalho[i][7] = cabecalho[i][7].strip()

#	for i in range(0,24):
#		print(cabecalho[i])

#lendo opticoes do arquivo
def read_option(name_file):
	f = open(name_file, "r")

	for i in range(24,172):
		aux = f.readline()
		option.append(aux.split(":"))
		#option[i][1] = option[i][1].strip()

	for i in range(24,172):
		print(i, option[i])

#lendo dados do arquivo
#def read_data(name_file):

#------------------------------------------------------------------------------

#main
name_file = raw_input('Nome do arquivo: ').strip();
#name_file = 'Tequila-completo.csv'

#leitura de cabecalho = validada
#read_reader(name_file)

#leitura de opcoes = erro 
#read_option(name_file)

read_all(name_file)
