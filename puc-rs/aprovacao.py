nota1 = float(input("Informe a primera nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
presenca = float(input("Informe a % de presença do aluno: "))
notaG1 = ((nota1 + nota2 + nota3)/3)

if presenca < 75:
    print("Aluno reprovado por faltas!")

elif notaG1 >= 7:
    print("Aluno aprovado em GRAU 1!")
else:
    print("O aluno devera realizar um exame de GRAU 2!")
    notaG2 = float(input("Informe a nota do Exame de Grau 2: "))
    mediaG1eG2 = (notaG1 + notaG2)/2

    if mediaG1eG2 >= 5:
        print("Aluno aprovado em GRAU 2!")
    else: print("Aluno reprovado em GRAU 2!")