def eh_primo(numero):
    cont = numero - 1
    primo = True
    while(cont > 1 and primo == True):
        if (numero % cont == 0):
            primo = False
        cont = cont - 1
    return primo

def maior_primo(numero):
    cont = 1
    numprimo = 1
    while(cont <= numero):
        ehprimo = eh_primo(cont)
        if (ehprimo):
            numprimo = cont
        cont = cont + 1
    return numprimo

def n_primos(numero):
    cont = 0
    inicial = 2    
    while(inicial <= numero):
        if (eh_primo(inicial)):
            cont += 1
        inicial += 1
    return cont
