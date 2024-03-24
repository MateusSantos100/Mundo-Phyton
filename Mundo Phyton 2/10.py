from random import randint
from time import sleep
itens=('Papel','Tesoura','Pedra')
computador=randint(0,2)
nome=str(input('Qual o seu nome: '))
print('Qual a sua jogada? \n0 Papel \n1 Tesoura \n2 Pedra')
print('-'*30)
jogador=int(input('Qual a sua jogada? '))
print('Computador jogou {} .'.format(itens[computador]))
print('Jogador jogou {} .'.format(itens[jogador]))
print('-'*30)
if computador==0:
    if jogador==0:
        print('empatou')
    elif jogador==1:
        print('Jogador Venceu')
    elif jogador ==2:
        print('Computador venceu')
    else:
        print('opção invalida')
elif computador == 1:
    if jogador == 1:
        print('Empatou')
    elif jogador == 0:
        print('Jogador perdeu')
    elif jogador == 2:
        print('Computador venceu')
    else:
        print('opção invalida')
elif computador == 2:
    if jogador==0:
        print('Jogador venceu')
    elif jogador ==1:
        print('Computador venceu')
    elif jogador == 2:
        print('empatou')
    else:
        print('opção invalida')