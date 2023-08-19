tipo_consumidor = input("Informe o tipo de consumidor (I para Industrial, C para Comercial, R para Residencial): ")
consumo = float(input("Informe a quantidade de energia consumida: "))

if tipo_consumidor == "I":
    valor_pago = 0.68 * consumo + 34
elif tipo_consumidor == "C":
    valor_pago = 0.37 * consumo + 45
elif tipo_consumidor == "R":
    valor_pago = 0.77 * consumo - 22
else:
    print("Tipo de consumidor inválido. Use 'I' para Industrial, 'C' para Comercial ou 'R' para Residencial.")
    valor_pago = None

if valor_pago is not None:
    print(f"O valor a ser pago é: R$ {valor_pago:.2f}")