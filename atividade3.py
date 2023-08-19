nome1 = input("Digite o nome da primeira pessoa: ")
idade1 = int(input(f"Digite a idade de {nome1}: "))

nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = int(input(f"Digite a idade de {nome2}: "))

ano_atual = int(input("Digite o ano atual (com 4 dígitos): "))

ano_nascimento1 = ano_atual - idade1
ano_nascimento2 = ano_atual - idade2

if idade1 < idade2:
    mais_nova = nome1
    ano_nova = ano_nascimento1
else:
    mais_nova = nome2
    ano_nova = ano_nascimento2

print(f"{mais_nova} é a pessoa mais nova e nasceu em {ano_nova}.")
