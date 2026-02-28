nota = float(input("Informe a nota do aluno: "))

if nota < 0 or nota > 100: print("Nota inválida")
else:
    if nota >= 90: conceito = "A"
    elif nota >= 80: conceito = "B"
    elif nota >= 70: conceito = "C"
    elif nota >= 60: conceito = "D"
    else: conceito = "F"
    print(f"O conceito do aluno é: {conceito}")