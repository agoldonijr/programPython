import socket

ip = raw_input("Ip:")
port = []
x = input("quantidade de portas")
i = 0

while(i<x):
	port.append(int (raw_input("Digite a porta: ")))
	i +=1
for p in port:
	cliente  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	cliente.settimeout(0.05)
	conexao = cliente.connect_ex((ip,p))
	print conexao
