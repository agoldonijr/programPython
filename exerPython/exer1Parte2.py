#Esse programa recebe um arquivo e retorna as estatisticas sobre ele
#numero de linhas, caracteres e palavras

import sys
import os.path

fn = raw_input('Nome do arquivo: ').strip()

if not os.path.exists(fn):
		print 'Tente novamente...'
		sys.exit()
a = open(fn).readlines()

print 'Total de linhas:', len(a)

chars = file(fn).read()

caracteres = len(chars)

print 'Numero de caracteres', caracteres

w = len(chars.split())

print 'Numero de palavras', w

