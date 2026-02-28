import math

horaInicio = int (input("Hora do início do jogo: "))
minutoInicio = int (input("Minuto do início do jogo: "))
horaFim = int (input("Hora do fim do jogo: "))
minutoFim = int (input("Minuto do fim do jogo: "))

if horaInicio >= 24 or horaInicio < 0:print("Horas do início inválidos")
if minutoInicio >= 60 or minutoInicio < 0:print("Minutos do início inválidos")
if horaFim >= 24 or horaFim <= 0:print("Horas do fim inválidos")
if minutoFim >= 60 or minutoFim < 0:print("Minutos do fim inválidos")

inicioTotal = horaInicio * 60 + minutoInicio
fimTotal = horaFim * 60 + minutoFim
if fimTotal > inicioTotal:
    duracaoTotal = fimTotal - inicioTotal
else:
    duracaoTotal = (1440 - inicioTotal) + fimTotal

horasDuracao = duracaoTotal // 60
restoMinutosDuracao = duracaoTotal % 60

print("O jogo durou: ",horasDuracao," horas, e ", restoMinutosDuracao," minutos")

if (math.fabs(horaFim - horaInicio)) > 1440:
    print("O jogo não pode durar mais de 24 horas!")