def maior_elemento(lista):
    valor = -999999
    for item in lista:
        if (item > valor):
            valor = item
    return valor
