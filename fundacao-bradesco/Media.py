def lerNotas():
    n = float(input("Digite a nota do aluno: "))
    return n

def resultado(n1,n2):
    media = (n1+n2)/2
    print("Nota 1 do aluno: ", n1)
    print("Nota 2 do aluno: ", n2)
    print("Média do aluno: ", media,"\nResultado: ",end="")
    if media >= 7:
        print("Aprovado")
    else: print("Reprovado")

a = lerNotas()
b = lerNotas()
resultado(a,b)