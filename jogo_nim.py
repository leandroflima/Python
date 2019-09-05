def computador_escolhe_jogada(n, m):
    valor_multiplo = (m + 1)

    sair = False
    total = n
    while(sair == False):
        if (total % valor_multiplo == 0):
            sair = True
        else:    
            total -= 1

    retorno = (n - total)

    if (retorno == 0):
      retorno = m
      
    if (retorno == 1):
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou {0} peças.".format(retorno))

    return retorno

def usuario_escolhe_jogada(n, m):
    ret = -1
    while(ret == -1):
        numero = int(input("Quantas peças você vai tirar? "))
        if (numero <=0 or numero > m or numero > n):
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
        elif (numero == 1):
            print()
            print("Você tirou uma peça.")
            ret = numero
        else:
            print()
            print("Voce tirou {0} peças.".format(numero))
            ret = numero

    return ret

def partida():
    print()
    n = int(input("Quantas peças? "))
    m = -1
    while(m == -1):
        num = int(input("Limite de peças por jogada? "))
        if (num < n):
            m = num
        else:
            print("Informe um valor menor que o total de peças: ", n)

    inicio = True
    computador = not (n % (m + 1) == 0)
    vencedor = 0
    while(n > 0):
        if (computador):
            if (inicio):
                print()
                print("Computador começa!")
                print()
            remov = computador_escolhe_jogada(n, m)
        else:
            if (inicio):
                print()
                print("Voce começa!")
                print()
            remov = usuario_escolhe_jogada(n, m)

        n = n - remov
        
        if (n == 1):
            print("Agora resta uma peça no tabuleiro.")
            print()
        elif (n > 1):
            print("Agora restam {0} peças no tabuleiro.".format(n))
            print()
        else:
            if (computador):
                print("Fim do jogo! O computador ganhou!")
                vencedor = 1
            else:
                print("Fim do jogo! Você ganhou!")
                vencedor = 2

        inicio = False        
        computador = not computador

    return vencedor

def campeonato():
    cont = 1
    voce = 0
    computador = 0
    while(cont <=3):
        print()
        print("**** Rodada {0} ****".format(cont))
        vencedor = partida()
        if (vencedor == 1):
            computador += 1
        else:
            voce += 1
        cont += 1

    print()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você {0} X {1} Computador".format(voce, computador))

    
def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    print()
    escolha = int(input())

    if (escolha == 1):
        print("Voce escolheu uma partida isolada!")
        partida()
    else:
        print("Voce escolheu um campeonado!")
        campeonato()

main()
