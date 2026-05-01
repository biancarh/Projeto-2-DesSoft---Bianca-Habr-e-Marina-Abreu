#importar as funcoes
from funcoes import *
#Listas auxiliares
lista_combinacoes=["1","2","3","4","5","6","sem_combinacao","quadra","full_house","sequencia_baixa","sequencia_alta","cinco_iguais"]
lista_combinacoes_usadas=[]
#Para iniciar temos que mostrar a cartela de pontos
      #FAZER
#São 12 rodadas
for rodada in range (12):
    #1-Início da rodada
    dados_rolados= rolar_dados(5)
    dados_guardados= []
    rerrolagens=0
    #2-Faço o loop da rodada (é infinito pois eu quebro quando ele digitar 0) 
    while True:    
        print(dados_rolados)
        print (dados_guardados)
        acao=int(input("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:"))
        if acao==1:
            d_guardado=int(input("Digite o índice do dado a ser guardado (0 a 4):"))
            #Essa lista tem duas posições: lista dos rodados e a lista dos guardados
            lista=guardar_dado(dados_rolados, dados_guardados, d_guardado)
            dados_rolados=lista[0]
            dados_guardados=lista[1]
        elif acao==2:
            d_removido=int(input("Digite o índice do dado a ser removido (0 a 4):"))
            #Essa lista tem duas posições: lista dos rodados e a lista dos guardados
            lista=remover_dado(dados_rolados, dados_guardados, d_removido)
            dados_rolados=lista[0]
            dados_guardados=lista[1]
        elif acao==3:
            if rerrolagens<=2:
                #São rolados apenas os que não estão guardados
                rerrolagens+=1
                quant=len(dados_rolados) #quant de dados disponíveis
                dados_rolados=rolar_dados(quant) #nova lista
            else:
                print ("Você já usou todas as rerrolagens.")
        elif acao==4:
            #Imprimir a cartela (não sei usar a funcao)
            cartela= 
        elif acao==0:
            print("Digite a combinação desejada:") #Só aparece quando digita 0 e não aparece quando a comb é inválida
            #Fiz um loop infinito pois, enquanto o usuário não digitar certo, ele continuará digitando sem nenhuma mensagem de input
            while True:
                comb=input()
                if comb not in lista_combinacoes:
                    print ("Combinação inválida. Tente novamente.")
                elif comb in lista_combinacoes_usadas:
                    print ("Essa combinação já foi utilizada.")
                else:
                    #Atualizo os pontos na cartela
                    #Atualizo os pontos para a pontuação final
                    lista_combinacoes_usadas.append(comb)
                    break #quebro o loop infinito que está dentro do elif==0
            break #Encerro a rodada
        else:
            print ("Opção inválida. Tente novamente.")

#3-Calculo a pontuação total e verifico se tem bônus
#4-Imprimo a cartela e a pontuação total

#FALTA FAZER A CONTAGEM DOS PONTOS
            


