media  = int(input("Digite a média do aluno: "))
faltas = int(input("Digite o número de faltas do aluno: "))

if media >= 7:
    if faltas <= 32:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado por faltas"
else:
    if faltas <= 32:
        resultado = "Reprovado por média"
    else:
        resultado = "Reprovado por faltas e por média"

print(resultado)

