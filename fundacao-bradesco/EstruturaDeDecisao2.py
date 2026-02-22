notaPrimeiroSem = float (input("Digite a sua primeira nota: "))
notaSegundoSem = float (input("Digite a sua segunda nota: "))

media = (notaPrimeiroSem + notaSegundoSem) / 2
if media >= 7:
    print("Você passou de ano")
else:
    diferença = float (abs(media - 7))
    print("Você reprovou de ano por", diferença, "pontos na média")