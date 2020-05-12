from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
results = (
    'EMPATE!',
    'JOGADOR VENCEU!',
    'COMPUTADOR VENCEU!',
    'JOGADA INVÁLIDA!'
)

computador = randint(0, 2)
print('''Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
 ''')

jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('JO!')
print('-=' * 11)
print('Jogador jogou {}'.format(itens[jogador])),
print('Computador jogou {}'.format(itens[computador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print(results[0])
    elif jogador == 1:
        print(results[1])
    elif jogador == 2:
        print(results[2])
    else:
        print(results[3])
elif computador == 1:
    if jogador == 0:
        print(results[2])
    elif jogador == 1:
        print(results[0])
    elif jogador == 2:
        print(results[1])
    else:
        print(results[3])
elif computador == 2:
    if jogador == 0:
        print(results[1])
    elif jogador == 1:
        print(results[2])
    elif jogador == 2:
        print(results[0])
    else:
        print(results[3])
