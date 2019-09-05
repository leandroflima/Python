import math

ponto1_coordenada_x_str = input("Digite a coordenada x do ponto 1: ")
ponto1_coordenada_y_str = input("Digite a coordenada y do ponto 1: ")
ponto2_coordenada_x_str = input("Digite a coordenada x do ponto 2: ")
ponto2_coordenada_y_str = input("Digite a coordenada y do ponto 2: ")

ponto1_coordenada_x = int(ponto1_coordenada_x_str)
ponto1_coordenada_y = int(ponto1_coordenada_y_str)
ponto2_coordenada_x = int(ponto2_coordenada_x_str)
ponto2_coordenada_y = int(ponto2_coordenada_y_str)

coordenadax = (ponto1_coordenada_x - ponto2_coordenada_x) ** 2
coordenaday = (ponto1_coordenada_y - ponto2_coordenada_y) ** 2
distancia = math.sqrt(coordenadax + coordenaday)

if (distancia >= 10):
    print("longe")
else:
    print("perto")



