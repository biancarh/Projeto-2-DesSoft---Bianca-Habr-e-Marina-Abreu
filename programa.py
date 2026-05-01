#importar as funcoes
from funcoes import *
#Listas auxiliares
lista_combinacoes=["1","2","3","4","5","6","sem_combinacao","quadra","full_house","sequencia_baixa","sequencia_alta","cinco_iguais"]
lista_combinacoes_usadas=[]
#Para iniciar temos que mostrar a cartela de pontos
contador = 0
cartela = {
    'regra_simples': {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
imprime_cartela(cartela)
#São 12 rodadas
for rodada in range(12):
    #1-Início da rodada
    dados_rolados= rolar_dados(5)
    dados_guardados= []
    rerrolagens=0
    x = 0
    #2-Faço o loop da rodada (é infinito pois eu quebro quando ele digitar 0) 
    while True:  
        if x == 0:
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        acao = input()

        if acao not in ["0","1","2","3","4"]:
            print("Opção inválida. Tente novamente.")
            x = 1
            continue
        x = 0
        
        if acao == "0":
            print("Digite a combinação desejada:")
            comb = input()
            while comb not in lista_combinacoes or comb in lista_combinacoes_usadas:
                if comb not in lista_combinacoes:
                    print("Combinação inválida. Tente novamente.")
                else:
                    print("Essa combinação já foi utilizada.")
                comb = input()
            dados_totais = dados_rolados + dados_guardados
            cartela = faz_jogada(dados_totais, comb, cartela)
            lista_combinacoes_usadas.append(comb)
            break  # SAI SEM imprimir de novo

        elif acao=="1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            d_guardado=int(input())
            #Essa lista tem duas posições: lista dos rodados e a lista dos guardados
            lista=guardar_dado(dados_rolados, dados_guardados, d_guardado)
            dados_rolados=lista[0]
            dados_guardados=lista[1]
        elif acao=="2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            d_removido=int(input())
            #Essa lista tem duas posições: lista dos rodados e a lista dos guardados
            lista=remover_dado(dados_rolados, dados_guardados, d_removido)
            dados_rolados=lista[0]
            dados_guardados=lista[1]
        elif acao=="3":
            if rerrolagens<2:
                #São rolados apenas os que não estão guardados
                rerrolagens+=1
                quant=len(dados_rolados) #quant de dados disponíveis
                dados_rolados=rolar_dados(quant) #nova lista
            else:
                print ("Você já usou todas as rerrolagens.")
        elif acao=="4":
            #Imprimir a cartela de pontos
            imprime_cartela(cartela)

        else:
            print ("Opção inválida. Tente novamente.")
        

#3-Calculo a pontuação total e verifico se tem bônus
contagem_pontos_total=0
contagem_pontos_regra_simples=0
for chave in cartela:
    for chave2 in cartela[chave]:
        if cartela[chave][chave2]!=-1:
            contagem_pontos_total+=cartela[chave][chave2]
            if chave == 'regra_simples':
                contagem_pontos_regra_simples+=cartela[chave][chave2]
if contagem_pontos_regra_simples>=63:
    contagem_pontos_total+=35

#4-Imprimo a cartela e a pontuação total
imprime_cartela(cartela)
print(f"Pontuação total: {contagem_pontos_total}")
   


