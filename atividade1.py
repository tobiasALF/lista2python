salario       = float(input("Digite o valor do salário: "))
financiamento = float(input("Digite o valor do financiamento pretendido: "))

if financiamento <= 5 * salario:
    print("Financiamento Concedido")
else:
    print("Financiamento Negado")

print("Obrigado por nos consultar.")