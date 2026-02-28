saldoMedio = float(input("Informe seu saldo médio: "))

if saldoMedio < 500 : print("Sem limite de crédito algum")
else:
    if saldoMedio >= 500 and saldoMedio < 1000 : creditoLimite = 1.08 * saldoMedio
    if saldoMedio >= 1000 : creditoLimite = 1.15 * saldoMedio
    print("Limite de crédito de: ", creditoLimite)

