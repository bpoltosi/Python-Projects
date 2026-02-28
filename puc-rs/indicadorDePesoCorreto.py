altura = float (input("Digite sua altura: "))
if altura <= 0:
    print("Comando de altura invalido")
if altura > 0:
    genero = int( input("Selecione seu genero: (1 para Masculino  ou 2 para Feminino) "))
    if genero != 1 and genero !=2:
        print("Comando de genero invalido")
    if genero == 1:
        pesoIdeal = 72.7 * altura - 58
        print("Seu peso ideal é de: " ,pesoIdeal, "kg")
    if genero == 2:
        pesoIdeal = 62.1 * altura - 44.7
        print("Seu peso ideal é de: ", pesoIdeal, "kg")
