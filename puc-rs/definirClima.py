temperatura = float(input("Digite a temperatura atual: "))
umidade = float(input("Digite a % relativa a umidade: "))

if umidade > 60:
    statusAr = str("umido")
else:
    statusAr = str("seco")


if temperatura >= 30:
    print("Clima muito quente e", statusAr)

elif 20 <= temperatura < 30:
    print("Clima quente e", statusAr)


elif 10 <= temperatura < 20:
    print("Clima ameno e", statusAr)

elif temperatura < 10: print("Clima frio e", statusAr)