import random
def rolar_dados(n):
    lista_resposta=[]
    for i in range (0,n):
        num_sorteado= random.randint(1,6)
        lista_resposta.append(num_sorteado)
    return lista_resposta

def guardar_dado(rolados, guardados, indice):
    dado_a_ser_guardado= rolados[indice]
    guardados.append(dado_a_ser_guardado)
    saida_rolados=[]
    for i in range (len(rolados)):
        if i!=indice:
            saida_rolados.append(rolados[i])
    return [saida_rolados, guardados]

def remover_dado(rolados,estoque,indice):
    dado_a_ser_removido=estoque[indice]
    rolados.append(dado_a_ser_removido)
    saida_estoque=[]
    for i in range (len(estoque)):
        if i!=indice:
            saida_estoque.append(estoque[i])
    return [rolados, saida_estoque]

def calcula_pontos_regra_simples(lista_rolados):
    dic_resposta={}
    for numero in range (1,7):
        pontuacao=0
        for dado in lista_rolados:
            if dado==numero:
                pontuacao+=numero
        dic_resposta[numero]=pontuacao
    return dic_resposta

def calcula_pontos_soma(x):
    soma = 0
    for numero in x:
        soma += numero
    return soma

def calcula_pontos_sequencia_baixa(x):
    sequencia = 0
    if 1 in x and 2 in x and 3 in x and 4 in x:
        sequencia = 1
    elif 2 in x and 3 in x and 4 in x and 5 in x:
        sequencia = 1
    elif 3 in x and 4 in x and 5 in x and 6 in x:
        sequencia = 1
    else:
        sequencia = 0
    if sequencia == 1:
        return 15
    else:
        return 0

def calcula_pontos_sequencia_alta(x):
    sequencia = 0
    if 1 in x and 2 in x and 3 in x and 4 in x and 5 in x:
        sequencia = 1
    elif 2 in x and 3 in x and 4 in x and 5 in x and 6 in x:
        sequencia = 1
    else:
        sequencia = 0
    if sequencia == 1:
        return 30
    else:
        return 0

def calcula_pontos_full_house(x):
    soma = 0
    numero1 = x[0]
    soma_numero1 = 0
    soma_numero2 = 0
    lista_numero2 = []
    for i in x:
        if i == numero1:
            soma_numero1 += 1
        else:
            lista_numero2.append(i)
            soma_numero2 += 1
        soma = soma + i

    if soma_numero2 == 3:
        if lista_numero2[0] == lista_numero2[1] == lista_numero2[2]:
            soma_numero2 = 10

    if soma_numero2 == 2 and soma_numero1 == 3:
        primeiro_elemento_lista_numero2 = lista_numero2[0]
        segundo_elemento_lista_numero2 = lista_numero2[1]
        if primeiro_elemento_lista_numero2 == segundo_elemento_lista_numero2:
            soma_numero2 = 10

    if (soma_numero1 == 3 and soma_numero2 == 10) or (soma_numero1 == 2 and soma_numero2 == 10):
        return soma
    else:
        return 0
