numero = int(input("Digite um número inteiro:"))
fatorial = numero
if (numero == 0):
    fatorial = 1
while(numero > 1):
    fatorial = fatorial * (numero - 1)
    numero = numero - 1
    
print(fatorial)
