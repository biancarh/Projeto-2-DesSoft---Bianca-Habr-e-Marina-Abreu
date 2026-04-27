import random
def rolar_dados(n):
    lista_resposta=[]
    for i in range (0,n):
        num_sorteado= random.randint(1,6)
        lista_resposta.append(num_sorteado)
    return lista_resposta
