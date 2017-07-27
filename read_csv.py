import csv
import sys
import os.path

dado = []
cabecalho = []
option = []

#lendo header do arquivo
def read_reader(name_file):
	f = open(name_file, "r")
	count = 0
	#lendo as 24 primeiras linhas e salvando no 
	for i in open(name_file, "r"):
		if count < 24:
			aux = f.readline()
			cabecalho.append(aux.split(":"))
			cabecalho[count][1] = cabecalho[count][1].strip()
			cabecalho[count][2] = cabecalho[count][2].replace("Sampling frequency", "").strip()
			cabecalho[count][3] = cabecalho[count][3].replace("Number of points","").strip()
			cabecalho[count][4] = cabecalho[count][4].replace("X start","").strip()
			cabecalho[count][5] = cabecalho[count][5].replace("Unit","").strip()
			cabecalho[count][6] = cabecalho[count][6].replace("Domain Unit","").strip()
			cabecalho[count][7] = cabecalho[count][7].strip()
		elif(count>=24 and count < 172):
			aux = f.readline()
			option.append(aux.split(":"))
			option[count-24][1] = option[count-24][1].strip()
		elif(count == 172):
			dado.append(f.readline)
		else:
			dado.append(f.readline())
		count+=1

	#print(cabecalho)
	for i in dado:
		print(i)

#------------------------------------------------------------------------------

#main

name_file = input('Nome do arquivo: ').strip();
#name_file = 'Tequila-completo.csv'

#leitura de cabecalho = validada
read_reader(name_file)

#leitura de opcoes = erro 
#read_option(name_file)

