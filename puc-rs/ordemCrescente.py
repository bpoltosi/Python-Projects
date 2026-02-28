valor1 = int(input("Digite o 1º valor: "))
valor2 = int(input("Digite o 2º valor: "))
valor3 = int(input("Digite o 3º valor: "))

if valor1 > valor2 and valor1 > valor3:               #Valor 1
    print(valor1, "é o maior número")

    if valor2 > valor3:
        print(valor2, "é o 2° maior número")
        print(valor3, "é o menor número")
    else:
        print(valor3, "é o 2° maior número")
        print(valor2, "é o menor número")

elif valor2 > valor1 and valor2 > valor3:            #valor 2
    print(valor2, "é o maior número")
    if valor1 > valor3:
        print(valor1, "é o 2° maior número")
        print(valor3, "é o menor número")
    else:
        print(valor3, "é o 2° maior número")
        print(valor2, "é o menor número")

else:                                   #Valor 3 (não precisa condicionar)
    print(valor3, "é o maior número")
    if valor1 > valor2:
        print(valor1, "é o 2° maior número")
        print(valor2, "é o menor número")
    else:
        print(valor2, "é o 2° maior número")
        print(valor1, "é o menor número")