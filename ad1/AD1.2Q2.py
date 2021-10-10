# Subprogramas
# Função para
# Função recursiva para solução da Torre de 3 pinos
def hanoiTresPinos(ndiscos, origem, destino, trabalho, qtdMov):
    if ndiscos==1: # Caso Base n = 1
        print('Mova disco {} do pino {} para o pino {}'.format(ndiscos, origem, destino))
    else: # Caso n > 1
        hanoiTresPinos(ndiscos - 1, origem, trabalho, destino, qtdMov) # chamada recursiva colocando pino trabalho como destino
        print('Mova disco {} do pino {} para pino {}'.format(ndiscos, origem, destino))
        hanoiTresPinos(ndiscos - 1, trabalho, destino, origem, qtdMov) # chamada recursiva colocando pino de trabalho como origem
    qtdMov.append(1) # adicionando contagem de chamada recursiva numa lista
    return len(qtdMov) # Retornando o tamanho da lista reprensentando a quantidade de chamadas
# Função recursiva para solução da Torre de 3 pinos
def hanoiQuatroPinos(ndiscos, origem, destino, trabalho, trabalho2, qtdMov):
    if ndiscos == 0:
        return None
    if ndiscos == 1: # Caso base n = 1
        print('Mova disco {} do pino {} para o pino {}'.format(ndiscos, origem, destino))
        qtdMov.append(1) # Adiciona a chamada recursiva na lista contadora
        return None
    else: # Caso n > 1
        hanoiQuatroPinos(ndiscos - 2, origem, trabalho, trabalho2, destino, qtdMov) # Chamada recursiva colocando pino de trabalho como destino
        qtdMov.append(1)
        print('Mova disco {} do pino {} para o pino {}'.format(ndiscos-1, origem, trabalho2))
        print('Mova disco {} do pino {} para o pino {}'.format(ndiscos, origem, destino))
        print('Mova disco {} do pino {} para o pino {}'.format(ndiscos-1, trabalho2, destino))
        hanoiQuatroPinos(ndiscos - 2, trabalho, destino, origem, trabalho2, qtdMov) # chamada recursiva colocando pino de trabalho como origem
        qtdMov.append(1)
    qtdMov.append(1)
    return len(qtdMov) # retornando o tamanho da lista representando a quantidade de chamadas
# Função para preencher Matriz 2 linhas e n colunas  onde a primeira linha representa  possíveis
# números de discos para a Torre de hanói, já a segunda linha representa a diferença de
# números de movimentos entre a torre de 3 pinos e a torre de 4 pinos
def preencheMatriz(tamCol):
    m = [] # iniciando a matriz
    for lin in range(1): # loop para preenhcer a primeira linha
        linha = []
        for col in range(1, tamCol+1): # loop para adicionar as colunas à primeira linha
            linha.append(col)
        m.append(linha) # adicionando a primeira linha na matriz com o métido append

    for lin in range(1): # Loop para preencher a segunda linha
        linha = []
        for col in range(1, tamCol+1): # loop para adicionar as colunas à segunda linha
# adicionando a diferença entre os movimentos de 3 e 4 pinos respectivamente a variável col itera de 1 até a última coluna
            linha.append((2 ** col - 1) - (2 * col - 1))
        m.append(linha) # adicionando a segunda linha a matriz
    return m # retornando a matriz

# Função para escrever a matriz 2 x n na saída padrão
def escreveMatriz(m, tamCol):
    for lin in range(2):
        for col in range(tamCol):
            print(' '*2, m[lin][col], end='  '*2) # adiciona um espaço * 2 no ínicio e no final de cada elemento da matriz
        print()

# Programa Principal
print('-='*35+'''
Informe um numero inteiro > 0 para representar a 
quantidade de discos para solução do jogo Torre de Hanói
'''+'-='*35)
qtdMov = [] # Inicializando lista contadora
qtdDiscos = int(input('Digite a quantidade de discos: ')) # Recebendo da entrada padrão valor reprensentando o número de discos para o jogo

while qtdDiscos <= 0: # Válido a entrada para que não seja menor ou igual a (0)
    print('Erro! Favor digitar uma quantidade válida\n') # Mensagem de erro ao usuário
    qtdDiscos = int(input('Digite a quantidade de discos: ')) #pedindo para entrar com valor válido só sairá do loop quando valor > 0

print('\nSolução para tabuleiro de 3 pinos:')
qtdMov3 = hanoiTresPinos(qtdDiscos, 'A', 'C', 'B', qtdMov) #Chamando função recursiva para o jogo com 3 pinos e guardando na variável qtdMov3 a quantidade de chamadas
print('Para resolver o jogo Torre de Hanoi com 3 pinos são necessários {} movimentos'.format(qtdMov3))

print('\nSolução para tabuleiro de 4 pinos:')
qtdMov = [] # zerando a lista contadora
qtdMov4 = hanoiQuatroPinos(qtdDiscos, 'A', 'D', 'B', 'C', qtdMov) # Chamando função recursiva para o jogo com 4 pinose guardando na variável qtdMov4 a quantidade de chamadas
print('Para resolver o jogo Torre de Hanoi com 4 pinos são necessários {} movimentos'.format(qtdMov4))

print('-='*45+'''
Informe um número inteiro para criação de matriz n x 2 contendo a quantidade de discos 
e a diferença da quantidade de  movimentos entre o tabuleiro com 3 pinos e 4 pinos 
'''+'-='*45)
tamColuna = int(input('Digite um número inteiro maior que (0): ')) # recebendo valor para quantidade lista de possíveis números de discos
while tamColuna <= 0: # validando entrada para que seja maior que (0)
    print('Erro! Favor digitar um valor inteiro maior que (0)\n')
    tamColuna = int(input('Digite um número inteiro: '))
matriz = preencheMatriz(tamColuna) # Chamando a função para preencher a matriz com os resultados
escreveMatriz(matriz, tamColuna) # Chamando a função para esrcrever a matriz na saída padrão
