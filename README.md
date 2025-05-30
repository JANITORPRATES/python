# Jogo da Velha

Este é um projeto simples de Jogo da Velha implementado em Python. O jogo permite que dois jogadores joguem alternadamente até que um ganhe ou empate.

## Funcionalidades

- Exibição do tabuleiro atualizado após cada jogada.
- Validação de jogadas para garantir que são dentro dos limites e em posições não ocupadas.
- Notificação de vitória para linhas, colunas e diagonais.
- Tratamento de exceções para entradas inválidas.
- Detecção de empate quando todas as posições estão preenchidas sem ganhador.

## Estrutura do Código

- `tabuleiro`: Lista aninhada representando o tabuleiro do jogo.
- `jogador`: Variável que indica o jogador atual ('X' ou 'O').

### Funções

- `exibeTabuleiro()`: Exibe o tabuleiro com formatação.
- `jogada(linha, coluna)`: Atualiza o tabuleiro com a jogada do jogador se a jogada for válida; alterna o jogador.
- `temGanhador()`: Verifica se há um ganhador e imprime uma mensagem.
- `temEmpate()`: Checa se o jogo terminou em empate.

## Como Jogar

1. Execute o script Python.
2. O console indicará qual é o jogador da vez.
3. Insira as coordenadas da sua jogada (linha e coluna) com valores de 0 a 2.
4. O jogo continuará alternando jogadores até que haja um ganhador ou empate.

## Requisitos

- Python 3.x

## Exemplo de Uso

Ao iniciar o jogo, siga as instruções no console para jogar. Insira os números correspondentes à linha e coluna desejadas para suas jogadas.

```shell
Jogador da vez: X
Digite a linha: 0
Digite a coluna: 1

Licença
Este projeto é de uso livre para fins educacionais e pessoais.
