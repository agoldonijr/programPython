import os

texto = 'Teste'

# cria um arquivo temporario
temp = os.tmpfile()

# escreve no arquivo
temp.write(texto)

# volta para o inicia do arquivo
temp.seek(0)

# conteudo do arquivo
print temp.read()

# fecha o arquivo
temp.close()