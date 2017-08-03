import csv
import matplotlib.pyplot as plt
import math

accX = []
accY = []
accZ = []
acc  = []

def calculate_acc():
	tem um laco aqui
	acc.append(sqrt(acc))	

def read_accX(name_file):
	for r in csv.reader(open(name_file, 'r')):
		accX.append(r)
def read_accY(name_file):
	for r in csv.reader(open(name_file, 'r')):
		accY.append(r)

def read_accZ(name_file):
	for r in csv.reader(open(name_file, 'r')):
		accZ.append(r)
##---------------------------------------------------------------------------##
##                          Funcao main                                      ##
##---------------------------------------------------------------------------##
#nome do arquivo para leitura
name_file = input('Nome do arquivo para X: ').strip()
read_accX(name_file)
#name_file = input('Nome do arquivo para Y: ').strip()
#read_accY(name_file)
#name_file = input('Nome do arquivo para Z: ').strip()
#read_accZ(name_file)
for i in accX:
	print (i)
