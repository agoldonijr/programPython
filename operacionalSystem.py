import os
import sys
import platform

def uid():
	"""
	uid() -> retorna a identificacao do usuario  corrente ou none se nao for possivel identificar
	"""

	# Variaveis de ambiente para cada SO
	us = {'Windows':'USERNAME','Linux':'USER'}

	u = us.get(platform.system())
	return os.environ.get(u)

print 'Usuario:', uid()
print 'plataforma:', platform.platform()
print 'Diretorio corrente:', os.path.abspath(os.curdir)
exep, exef = os.path.split(sys.executable)
print 'Executavel:', exef
print 'Diretorio do executavel:', exep