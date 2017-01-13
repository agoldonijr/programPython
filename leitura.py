import sys
import os.path

fn = raw_input('Nome do arquivo: ').strip()

if not os.path.exists(fn):
		print 'Tente novamente...'
		sys.exit()

# Numerando as linhas
# for i,s in enumerate(open(fn)):
	# print i+1, s,

a  = open('temp.txt').readlines()

print a[27]