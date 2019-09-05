import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    
    
    pass


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    soma_tamanho_palavras = 0
    sentencas = separa_sentencas(texto)
    todas_palavras = []
    total_caracteres_sentencas = 0
    total_caracteres_frases = 0
    total_frases = 0
    numero_sentencas = 0
    numero_total_palavras = 0
    for sentenca in sentencas:
        numero_sentencas += 1
        total_caracteres_sentencas += len(sentenca)
        frases = separa_frases(sentenca)
        for frase in frases:
            total_frases += 1
            total_caracteres_frases += len(frase)
            palavras = separa_palavras(frase)
            for palavra in palavras:
                numero_total_palavras += 1
                soma_tamanho_palavras += len(palavra)
                todas_palavras.append(palavra)

    tamanho_medio_palavra = soma_tamanho_palavras / numero_total_palavras    

    numero_palavras_diferentes = n_palavras_diferentes(todas_palavras)
    relacao_type_token = numero_palavras_diferentes / numero_total_palavras

    numero_palavras_unicas = n_palavras_unicas(todas_palavras)
    razao_hapax_legomana = numero_palavras_unicas / numero_total_palavras

    tamanho_medio_sentenca = total_caracteres_sentencas / numero_sentencas

    complexidade_sentenca = total_frases / numero_sentencas

    tamanho_medio_frase = total_caracteres_frases / total_frases
    
    return [tamanho_medio_palavra, relacao_type_token, razao_hapax_legomana, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    pass


def valida_teste_calcula_assinatura(texto, valor, esperado):
    if (float(valor) != float(esperado)):
        print("{0} errado! retornado:{1} esperado:{2}".format(texto, valor, esperado))


def teste_calcula_assinatura():
    texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
    retorno = calcula_assinatura(texto)

    print("inicio testes")
    valida_teste_calcula_assinatura("tamanho_medio_palavra", retorno[0], 5.571428571428571)
    valida_teste_calcula_assinatura("relacao_type_token", retorno[1], 0.8253968253968254)
    valida_teste_calcula_assinatura("razao_hapax_legomana", retorno[2], 0.6984126984126984)
    valida_teste_calcula_assinatura("tamanho_medio_sentenca", retorno[3], 210.0)
    valida_teste_calcula_assinatura("complexidade_sentenca", retorno[4], 4.5)
    valida_teste_calcula_assinatura("tamanho_medio_frase", retorno[5], 45.888888888888886)
    print("fim testes")
