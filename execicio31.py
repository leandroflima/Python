lista = [6,-2,7,0,-5,8,4]
for item in lista:
    resultado = item % 2
    if resultado == 0:
        print("Numero {item} é par!".format(item = item))
    else:
        print("Numero {item} é impar!".format(item = item))
