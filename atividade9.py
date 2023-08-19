sexo      = input("Informe o sexo (H para homem, M para mulher): ")
peso      = int(input("Informe o peso (kg): "))
altura_cm = int(input("Informe a altura (cm): "))
idade     = int(input("Informe a idade: "))

if sexo == "H":
    calorias_ideais = 66 + (13.7 * peso) + (5.0 * altura_cm) - (6.8 * idade)
    mensagem = "homens"
else:
    calorias_ideais = 665 + (9.6 * peso) + (1.8 * altura_cm) - (1.7 * idade)
    mensagem = "mulheres"

print(f"O valor ideal de calorias diárias para {mensagem} é: {calorias_ideais:.2f} calorias")