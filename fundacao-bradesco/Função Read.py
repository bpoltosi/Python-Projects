arquivo = open('arquivo.txt','w')

arquivo.write('Arquivo de texto\n')
arquivo.write('Aula prática')
arquivo.close()

leitura = open('arquivo.txt','r')
print(leitura.read())
close = open('arquivo.txt','w')