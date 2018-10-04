# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 08:54:17 2018
EP1
@author: Guilherme Boldin
"""
#from firebase import firebase
#firebasecardápio = firebase.FirebaseApplication('https://ep1-dsoft-aaf53.firebaseio.com/', None)
##firebasecomandas =
#if firebasecardápio.get("cardápio",None) is None:                
#    cardápio = {}
#else:
#    cardápio= firebasecardápio.get("cardápio",None)
# definição de cardápio
import json
with open('file.txt','r') as f:
    cardápio=json.load(f)

comandas={}
while True:
    #introdução do programa
    print('\nComanda eletrônica:')
    print('\n0 = sair e salvar\n1 = imprimir e gerenciar cardápio\n2 = adicionar item a comanda\n3 = remover item da comanda\n4 = imprimir comanda ')   #p1
    a=int(input('Faça a sua escolha: '))
        #opção 0: cancelar
    if a==0:
        print('Até mais')
        break
        
        #opção 1: mostra o cardápio e o preço de cada item do cardápio, além de gerenciar o cardápio.
    if a==1:
        print('O cardápio possui os seguintes itens: ')
        for chave in cardápio:
            print('-{0}  (R${1:.2f})'.format(chave,cardápio[chave]))
        escolha=int(input('Você deseja alterar o cardápio?\n1 = Sim\n2 = Não\nSua escolha: '))
        if escolha== 1:
                escolha2=int(input('Deseja adicionar, remover ou mudar itens do cardápio?\n1 - Adicionar\n2 - Remover\n3 - Mudar\nSua escolha: '))
                if escolha2 == 1:
                    adicionaritem=input('Digite o item: ')
                    adicionarpreço=float(input('Digite o preço do produto: '))
                    print("O produto foi adicionado assim como o preço!")
                    #for chave in cardápio:
                            #print('-{0}  (R${1:.2f})'.format(chave,cardápio[chave]))
                    if adicionarpreço<0:
                        print('Por favor, insira um preço válido')
                    cardápio[adicionaritem]=adicionarpreço
                    for chave in cardápio:
                        print('-{0}  (R${1:.2f})'.format(chave,cardápio[chave]))
                if escolha2 == 2:
                    removeritem=input('Digite o item a ser removido: ')
                    if removeritem not in cardápio:
                        print("Por favor, insira um elemento que existe no cardápio")
                    del cardápio[removeritem]
                    for chave in cardápio:
                           print('-{0}  (R${1:.2f})'.format(chave,cardápio[chave]))
                if escolha2 ==3 :
                    nomedoprodutoasermudado=input('Digite o nome do produto a ter o preço mudado:')
                    if nomedoprodutoasermudado in cardápio:
                        novopreço=float(input('Digite o preço novo: '))
                        cardápio[nomedoprodutoasermudado]=novopreço
                        for chave in cardápio:
                            print('-{0}  (R${1:.2f})'.format(chave,cardápio[chave]))
                    else:
                        print("Por favor, insira um produto do cardápio")
    if a==2: #add item
        print(cardápio)
        comanda=input("Digite a comanda que deseja adicionar um item: ")
        if comanda in comandas: 
            produto=input("Digite o nome do produto: ")
            if produto in cardápio:
                if produto not in comandas[comanda].keys():
                    quantidade=int(input("Digite a quantidade que deseja inserir: "))
                    comandas[comanda].update({produto:quantidade})
                else:
                    quantidade=int(input("Digite a quantidade que deseja inserir: "))+comandas[comanda][produto]
                    comandas[comanda].update({produto:quantidade})
            else:
                print("Por favor, insira um produto do cardápio")                        
        if comanda not in comandas:
            produto=input("Digite o nome do produto: ")
            quantidade=int(input("Digite a quantidade que deseja inserir: "))
            comandas[comanda]={produto:quantidade}
            if quantidade < 0:
                print("Por favor, insira uma quantidade maior que zero:")


        print(comandas)
    if a==3:                 #remove item
        print(cardápio)
        comanda=input("Digite a comanda que deseja remover um item: ")
        if produto in cardápio:
            if comanda in comandas: 
                produto=input("Digite o nome do produto: ")
                quantidade=abs(int(input("Digite a quantidade que deseja remover: "))-comandas[comanda][produto])
                comandas[comanda].update({produto:quantidade})
                print(comandas)
    if a==4:
        nomedacomanda=input("Insira qual comanda você deseja imprimir: ")
        print("A comanda {0} contém os seguintens produtos:".format(nomedacomanda))
        somatudo=[]
        for keys in comandas[nomedacomanda]:
            print('\n- '+keys+': '+str(comandas[nomedacomanda][keys]).format(keys,comandas[nomedacomanda][keys]))
            print('Preço unitário: R${0:.2f}'.format(cardápio[keys]))
            print('Preço total: R${0:.2f}'.format(comandas[nomedacomanda][keys]*cardápio[keys]))
            brisa=comandas[nomedacomanda][keys]*cardápio[keys]
            somatudo.append(brisa)
        print('TOTAL: {0:.2f}'.format(sum(somatudo)))
        dezporcento=((sum(somatudo))*1.1)
        print('TOTAL (c/10%): {0:.2f}'.format(dezporcento))
            
    
    if a>4 or a<0:
        print('Por favor, escolha uma opção vállida entre 0 e 4.')

with open('file.txt', 'w') as file:
    json = json.dumps(cardápio)
    cardápio=file.write(json)
#result = firebase.patch('https://ep1-dsoft-aaf53.firebaseio.com/cardápio', cardápio)
        