
tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
jogador = 'X'

def exibeTabuleiro():
    for linha in tabuleiro:
       print('|'.join(linha))
       print('-'*6)

def jogada(linha, coluna):
    if (
        not 0 <= linha <= 2 or
        not 0 <= coluna <= 2 or 
        tabuleiro[linha][coluna] != ' '
    ):
        print('Jogada inválida!')
        return jogador
    
    tabuleiro[linha][coluna] = jogador
    return 'O' if jogador == 'X' else 'X'

while True:
    print(f'Jogador da vez: {jogador}')
    try:
        linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna: '))
        jogador = jogada(linha, coluna)
    except IndexError:
        print('Digite valores numéricos entre 0 e 2')
    except ValueError:
        print('Os valores devem ser números inteiros')


    exibeTabuleiro()


