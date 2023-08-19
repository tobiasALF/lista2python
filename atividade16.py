numero = int(input("Informe um número de 3 dígitos: "))

if 100 <= numero <= 999:
    digito1 = numero // 100
    digito2 = (numero // 10) % 10
    digito3 = numero % 10

    soma_digitos = digito1 + digito2 + digito3

    print(f"Soma dos dígitos do número {numero} é igual a {soma_digitos}")

    novo_numero = digito1 * 100 + digito2 * 10 + digito3

    if novo_numero % 16 == 0 and novo_numero % 4 == 0:
        print("O número informado é divisor de 16 e múltiplo de 4 ao mesmo tempo.")
    else:
        print("O número informado não satisfaz as condições.")
else:
    print("Número fora do intervalo de três dígitos.")