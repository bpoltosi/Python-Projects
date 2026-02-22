quantidade = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while valor > 0.0:
    soma += valor
    quantidade += 1
    valor = float(input("Digite um valor: "))

media = soma / quantidade
print("Total da soma: ", soma)
print("Quantidade de numeros digitados: ", quantidade)
print("Media dos numeros digitados: ", media)