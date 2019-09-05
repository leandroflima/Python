numerostr = input("Digite um número: ")

numero = int(numerostr)

if (numero % 3 == 0) and (numero % 5 == 0):
    print("FizzBuzz")
else:
    print(numero)
