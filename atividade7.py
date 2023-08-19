angulo1 = int(input("Digite o valor do primeiro ângulo: "))
angulo2 = int(input("Digite o valor do segundo ângulo: "))
angulo3 = int(input("Digite o valor do terceiro ângulo: "))

soma_angulos = angulo1 + angulo2 + angulo3

if soma_angulos == 180:
    if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
        resultado = "Acutângulo"
    elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        resultado = "Retângulo"
    elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        resultado = "Obtusângulo"
else:
    resultado = "Os ângulos informados não formam um triângulo"

print(resultado)