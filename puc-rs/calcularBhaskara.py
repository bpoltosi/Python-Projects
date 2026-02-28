import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
deltaBhaskara = float((b*b) - (4*a*c))

if deltaBhaskara < 0:
    print("Delta negativo, a equação nao possui raízes reais ")

else:
    raizDelta = math.sqrt(deltaBhaskara)
    x1 = (-b + raizDelta)/(2*a)

    if deltaBhaskara == 0:
        print("Há apenas uma raiz real ", x1)
    else:
        x2 = (-b - raizDelta)/(2*a)
        print("Há duas raizes reais, seus valores são: ", x1, x2)