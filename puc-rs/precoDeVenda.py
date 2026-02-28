precoDeCusto = float(input("Informe o preço de custo: "))

if precoDeCusto < 0: print("Erro no preço de custo!")
else:
    if precoDeCusto < 10 and precoDeCusto > 0: taxaDeLucro = 70/100
    if precoDeCusto > 10 and precoDeCusto < 30: taxaDeLucro = 50/100
    if precoDeCusto > 30 and precoDeCusto < 50: taxaDeLucro = 40/100
    if precoDeCusto >= 50: taxaDeLucro = 30/100
    valorDeVenda = (precoDeCusto * taxaDeLucro) + precoDeCusto
    print("----------------------------------")
    print("Preço de custo: ",precoDeCusto)
    print("Valor de venda: ",valorDeVenda)
    print("----------------------------------")