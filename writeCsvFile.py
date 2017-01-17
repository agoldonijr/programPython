import csv

# Modo de descrito de arquivos csv
# dados
dt = (('temperatura',15.0,'C','10:40','2016-12-31'),('peso',42.5,'kg', '10:45', '2016-12-31'))

#A rotina de escreta recebe um objeto do tipo file
out = csv.writer(file('dt.csv','w'))

#escrevendo as tuplas no arquivo
out.writerows(dt)