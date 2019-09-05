largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

for y in range(altura):
    for x in range(largura):
        if (x == 0 or x == largura - 1 or y == 0 or y == altura - 1):
            print("#", end = "")
        else:
            print(" ", end = "")
    print("", end = "\n")
    
