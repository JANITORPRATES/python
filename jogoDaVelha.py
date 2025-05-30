"""

tabuleiro = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
"""
tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
jogador = 'X'

def exibeTabuleiro():
    for linha in tabuleiro:
       print('|'.join(linha))
       print('-'*6)
       #print(f'{linha[0]}|{linha[1]}|{linha[2]}')

def jogada(linha, coluna):
    tabuleiro[linha][coluna] = jogador
    if jogador == 'X':
        return 'O'
    else:
        return 'X'

jogada(1,1)
jogada(2,1)
jogada(1,0)


exibeTabuleiro()

