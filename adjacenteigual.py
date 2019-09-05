numero = input("Digite um número inteiro: ")

anterior = 0
resultado = "não"
for digito in numero:
    if (int(digito) == anterior):
        resultado = "sim"
    else:
        anterior = int(digito)

print(resultado)
