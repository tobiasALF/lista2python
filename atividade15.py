hora_inicial   = int(input("Hora inicial do jogo: "))
minuto_inicial = int(input("Minuto inicial do jogo: "))
hora_final     = int(input("Hora final do jogo: "))
minuto_final   = int(input("Minuto final do jogo: "))

if hora_inicial > 24 or hora_final > 24 or minuto_inicial > 59 or minuto_final > 59:
    print("Entrada de dados não é válida.")
else:
    duracao_horas = hora_final - hora_inicial
    duracao_minutos = minuto_final - minuto_inicial

    if duracao_minutos < 0:
        duracao_horas -= 1
        duracao_minutos += 60

    print(f"Duração do jogo: {duracao_horas} hora(s) e {duracao_minutos} minuto(s)")