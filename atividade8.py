distancia_km    = int(input("Digite a distância percorrida em Km: "))
litros_gasolina = int(input("Digite a quantidade de litros de gasolina consumidos: "))

consumo_km_por_litro = distancia_km / litros_gasolina

mensagem = ""
if consumo_km_por_litro < 8:
    mensagem = "Venda o carro"
elif consumo_km_por_litro >= 8 and consumo_km_por_litro <= 14:
    mensagem = "Econômico!"
else:
    mensagem = "Super econômico!"

print(f"O consumo do carro é de {consumo_km_por_litro:.2f} Km/l. Mensagem: {mensagem}")