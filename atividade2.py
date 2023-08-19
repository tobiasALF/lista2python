distancia_carro1 = int(input("Digite a distância percorrida pelo primeiro carro: "))
tempo_carro1     = int(input("Digite o tempo levado pelo primeiro carro: "))

distancia_carro2 = int(input("Digite a distância percorrida pelo segundo carro: "))
tempo_carro2     = int(input("Digite o tempo levado pelo segundo carro: "))

velocidade_media_carro1 = distancia_carro1 / tempo_carro1
velocidade_media_carro2 = distancia_carro2 / tempo_carro2

if velocidade_media_carro1 > velocidade_media_carro2:
    print("O primeiro carro teve maior velocidade média.")
elif velocidade_media_carro2 > velocidade_media_carro1:
    print("O segundo carro teve maior velocidade média.")
else:
    print("Os dois carros tiveram a mesma velocidade média.")

