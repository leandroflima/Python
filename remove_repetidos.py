def remove_repetidos(lista):
    lista2 = []
    for item in lista:
        if (not item in lista2):
            lista2.append(item)
    lista2.sort()
    return lista2
