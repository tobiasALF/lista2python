nome  = input("Digite o nome do aluno: ")
nota1 = int(input("Digite a primeira nota do aluno: "))
nota2 = int(input("Digite a segunda nota do aluno: "))

media = (nota1 + nota2) / 2

if 0 <= media < 5:
    resultado = "Reprovado"
elif 5 <= media < 7:
    resultado = "Recuperação"
elif 7 <= media <= 10:
    resultado = "Aprovado"

print(f"Nome: {nome}")
print(f"Média: {media:.2f}")
print(resultado)