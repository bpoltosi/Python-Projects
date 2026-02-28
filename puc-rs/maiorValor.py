v1 = int(input("Insira o primeiro valor: "))
v2 = int(input("Insira o segundo valor: "))
v3 = int(input("Insira o terceiro valor: "))
v4 = int(input("Insira o quarto valor: "))

maior = v1
if v2 > maior : maior = v2
if v3 > maior : maior = v3
if v4 > maior : maior = v4

print("O maior valor é: " ,maior)