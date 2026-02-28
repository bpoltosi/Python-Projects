valorTotal = int (input("Insira um valor de 4 Dígitos: "))
valorMilhar = valorTotal // 1000
restoMilhar = valorTotal%1000
valorCentena = restoMilhar // 100
restoCentena = restoMilhar%100
valorDezena = restoCentena // 10
restoDezena = restoCentena%10
valorUnidade = restoDezena

print("Numeral do primeiro dígito: " + str(int(valorMilhar)))
print("Numeral do segundo dígito: " + str(int(valorCentena)))
print("Numeral do terceiro dígito: " + str(int(valorDezena)))
print("Numeral do quarto dígito: " + str(int(valorUnidade)))

#print('Valor invertido: ', valorUnidade*1000 + valorDezena*100 + valorCentena*10 + valorMilhar)
digitosInvertidos = int (((valorUnidade) * 1000) + ((valorDezena) * 100) + ((valorCentena) * 10) + ((valorMilhar)))
print("Numerais com dígitos invertidos: " +str(int(digitosInvertidos)))

