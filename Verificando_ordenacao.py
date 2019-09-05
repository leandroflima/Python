numero1str = input("Digite o primeiro número: ")
numero2str = input("Digite o segundo número: ")
numero3str = input("Digite o terceiro número: ")

numero1 = int(numero1str)
numero2 = int(numero2str)
numero3 = int(numero3str)

if ((numero1 < numero2) and (numero2 < numero3)):
    print("crescente")
else:
    print("não está em ordem crescente")
