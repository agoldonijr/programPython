import os.path
import glob

#mestra uma lista de nomes de arquivos e seus tamanhos

for arq in sorted(glob.glob('*.py')):
 	# a funcao glob.glob eh semelhando ao ls do unix, retornando os arquivos que possuim determinado criterio
	print arq, os.path.getsize(arq)