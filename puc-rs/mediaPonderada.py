nota1 = float(input("Informe a 1° nota: "))
nota2 = float(input("Informe a 2° nota: "))
nota3 = float(input("Informe a 3° nota: "))

if nota1 > 10 or nota1 < 0 or nota2 < 0 or nota2 > 10 or nota3 < 0 or nota3 > 10:
    print("Erro no informe das notas")
else:

v1 = nota1
v2 = nota2
v3 = nota3

if v2 < v1:
    aux = v1
    v1 = v2
    v2 = aux

if v3 < v1:
    aux = v1
    v1 = v3
    v3 = aux

if v3 < v2:
    aux = v2
    v2 = v3
    v3 = aux

menorNota = v1
notaMeio = v2
maiorNota = v3

mediaPonderada = ((maiorNota * 5) + (menorNota * 2.5) + (notaMeio * 2.5)) / 10
print("Média ponderada final: ", mediaPonderada)