sexo = input("Informe o sexo (M para masculino, F para feminino): ")
idade = int(input("Informe a idade: "))

if sexo == "M":
    if idade >= 21:
        print("Maior idade")
    else:
        print("Menor idade")
elif sexo == "F":
    if idade >= 18:
        print("Maior idade")
    else:
        print("Menor idade")
else:
    print("Sexo não reconhecido.")
