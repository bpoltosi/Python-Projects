dia = int(input("Digite o dia da semana (1 a 7): "))

if dia < 1 or dia > 7: print("Valor inválido, fora do intervalo")
else:
    if dia == 1: print("Domingo")
    if dia == 2: print("Segunda")
    if dia == 3: print("Terça")
    if dia == 4: print("Quarta")
    if dia == 5: print("Quinta")
    if dia == 6: print("Sexta")
    if dia == 7: print("Sábado")