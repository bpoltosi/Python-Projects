numero = int(input("Digite um número de 4 dígitos: "))
print("--------------------------------------------------")
if numero > 999 and numero < 10000:

    primeiroDigito = numero // 1000
    resto = numero % 1000

    segundoDigito = resto // 100
    resto = resto % 100

    terceiroDigito = resto // 10
    quartoDigito = resto % 10

    print("Primeiro dígito: ", primeiroDigito)
    print("Segundo dígito: ", segundoDigito)
    print("Terceiro dígito: ", terceiroDigito)
    print("Quarto dígito: ", quartoDigito)
    print("--------------------------------------------------")
    if primeiroDigito == quartoDigito and segundoDigito == terceiroDigito:
        print("Seu número é um Capicua")
    else:
        print("seu numero não é um Capicua")
    print("--------------------------------------------------")

else:
    print("Número invalido")
    print("--------------------------------------------------")