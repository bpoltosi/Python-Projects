nota = float (input("Escreva sua nota: "))
print("---------------------------------")
print("Sua nota é: ", nota)
print("---------------------------------")
if nota >=0 and nota <= 10:

    if nota >= 9 and nota <= 10:
        print("Seu conceito é A")
    if nota < 9 and nota >= 7:
        print("Seu conceito é B")
    if nota < 7 and nota >= 5:
        print("Seu conceito é C")
    if nota < 5 and nota >= 3:
        print("Seu conceito é D")
    if nota < 3 and nota >= 0:
        print("Seu conceito é E")

    print("---------------------------------")
else: print("Nota inválida")