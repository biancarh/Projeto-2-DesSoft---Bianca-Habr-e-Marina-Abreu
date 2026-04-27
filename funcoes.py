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

