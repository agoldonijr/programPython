#!/bin/python3

frase  		= 'eh nois brodi';
integer 	= 1;
real		= 1.1
realMaior	= 1.123456789

print('Comecando com frase')
print('frase: ', frase)
print('inteiro: ', integer)
print('real: ', real)
print('real maior: ', realMaior)

print('Podemos fazer um inteiro virar uma frase')
print('Integer: ', integer)
integer 	= 'eh nois aqui tbm'
print('Integer de novo: ', integer)


integer 	= 1;
print("Tambem podemos fazer casting de variaveis")
print(float(integer))


print("Temos tbm a opcao de numeros complexos")
c = 1 + 4j
print("c eh um numero complexo: ", c)
print("parte real ",c.real)
print("parte imaginaria " , c.imag)
print("Conjugado ",c.conjugate())
