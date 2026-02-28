import math

tempoTotalSegundos = float (input("Quantos segundos o evento durou: "))

tempoMinutos = tempoTotalSegundos / 60
tempoHoras = tempoTotalSegundos / (60 * 60)

restoHoras = (tempoTotalSegundos // (60 * 60))
restoMinutos = (tempoTotalSegundos% (60*60)) // 60
restoSegundos = (tempoTotalSegundos%60)

print("Tempo em horas: " + str(int(restoHoras)))
print("Tempo em minutos: " + str(int(restoMinutos)))
print("Tempo em segundos: " + str(int(restoSegundos)))