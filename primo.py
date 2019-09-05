numero = int(input("Digite um número inteiro: "))
cont = numero - 1
primo = True
while(cont > 1 and primo == True):
    if (numero % cont == 0):
        primo = False
    cont = cont - 1
if (primo):
    print("primo")
else:
    print("não primo")
