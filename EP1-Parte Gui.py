# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 08:54:17 2018
EP1
@author: Guilherme Boldin
"""
# definição de cardápio
cardápio={'jujuba':3, 'cachorro quente':5}
comanda={}
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
        print(cardápio)
        escolha=int(input('Você deseja alterar o cardápio?\n1 = Sim\n2 = Não\n'))
        if escolha== 1:
                escolha2=int(input('Deseja adicionar, remover ou mudar itens do cardápio?\n 1 - Adicionar\n 2 - Remover\n 3 - Mudar\n'))
                if escolha2 == 1:
                    adicionaritem=input('Digite o item: ')
                    adicionarpreço=int(input('Digite o preço novo: '))
                    if adicionarpreço<0:
                        print('Por favor, insira um preço válido')
                    cardápio[adicionaritem]=adicionarpreço
                if escolha2 == 2:
                    removeritem=input('Digite o item a ser removido: ')
                    if removeritem not in cardápio:
                        print("Por favor, insira um elemento que existe no cardápio")
                    del cardápio[removeritem]
                if escolha2 ==3 :
                    nomedoprodutoasermudado=input('Digite o nome do produto a ter o preço mudado:')
                    novopreço=int(input('Digite o preço novo: '))
                    cardápio[nomedoprodutoasermudado]=novopreço
    if a>4 or a<0:
        print('Por favor, escolha uma opção vállida entre 0 e 4.')