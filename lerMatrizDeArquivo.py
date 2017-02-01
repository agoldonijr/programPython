import os
import sys
fileName = raw_input('Nome do arquivo: ').strip()

if not os.path.exists(fileName):
		print 'Tente novamente...'
		sys.exit()

else:
	a  = open(fileName).readlines()

vetDim = a[0]
fator = a[1]

print vetDim, fator