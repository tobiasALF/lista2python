num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print("O maior número é:", num1)
elif num2 > num3:
    print("O maior numero é:", num2)
else:
    print("O maior numero é:", num3)

if num1 == num2 == num3:
    print("A quantidade de numeros são as mesmas!")
else:
    print("")


print("Fim do programa!")