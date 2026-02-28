ano = int(input("Digite um ano entre 1900 e 2099: "))

if ano < 1900 or ano > 2099:
    print("Informe um ano válido!")
else:
    a = ano % 19
    b = ano % 4
    c = ano % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    dia = 22 + d + e

    # Os anos 1954, 1981, 2049 e 2076 são exceções à fórmula
    # e necessitam a retirada de 7 dias do resultado
    if ano == 1954 or ano == 1981 or ano == 2049 or ano == 2076:
        dia = dia - 7

    if dia <= 31:
        print(f"Dia: {dia} de Março.")

    else: 
        print(f"Dia: {dia - 31} de Abril.")


