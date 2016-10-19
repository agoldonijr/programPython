#!/usr/bin/python3

#funcao que imprime a lista
def print_list(lista):
	for i in range(0, len(lista)):
		print(lista[i])

#criando uma lista simples
lista = ['a','b','c','d','e']
print_list(lista);

#adicionando um elemento a lista
lista.append('f');
print_list(lista);

#removendo elemento da lista
lista.remove('a')
print_list(lista);


#ordena a lista
lista.sort();

#inverte a lista
lista.reverse();

print(lista[0:])
