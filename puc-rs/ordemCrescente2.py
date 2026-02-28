v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))
v3 = int(input("Digite o terceiro valor: "))

maior = v1
if v2 > maior : maior = v2
if v3 > maior : maior = v3

menor = v1
if v2 < menor : menor = v2
if v3 < menor : menor = v3

meio = int((v1+v2+v3) - maior - menor)

print("Ordem crescente: ", menor,meio,maior)
print("Ordem decrescente: ", maior, meio, menor)