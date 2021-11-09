#AD2-1 - Questão 1 - Acácio Novoa Monteiro - 18213050070
#Subprogramas

# A função a seguir escreve uma martriz na tela
def escreveMatriz(m):
    cont = 0 # inicializa a variável contadora

    for i in m: # iterando sobre a matriz passada por parâmetro

        for lin in i: # iterando sobre cada elemento da matriz, ou seja, os itens mais internos da lista de listas

            print(f'{lin:^3}', end=' '*2) # exibindo na tela item por item em forma de matriz
            cont += 1 # variável contadora é icrementada a cada iteração dos elementos da matriz

        print()
    print(f'Quantidade de elementos: {cont}') # exibe a quantidade de elementos da matriz

# A função a seguir compara o tamanho de duas matrizes e retorna a matriz com mais elementos
def comparaMatriz(m1, m2):
    cont = cont2 = 0 # inicializando as variáveis contadoras

    for i in m1: # iterando sobre a primeira matriz passada por parâmetro
        for j in i: # iterando sobre cada elemendo da matriz,ou seja, os itens mais internos da listas de listas
            cont += 1 # a cada elemento iterando o contador é icrementado 1 a 1

# o trecho abaixo é análogo ao trehco acima, porém itera sobre a segunda matriz passada por parâmetro
    for i in m2:
        for j in i:
            cont2 +=1

    if cont > cont2: # verifica se a primeira matriz tem mais elementos do que a segunda
        return m1 # se a condição acima for verdadeira retorna a primeira matriz informada
    else:
        return m2 # se acondição acima for falsa retorna a segunda matriz informada

# A função a seguir gera uma matriz transposta de uma matriz passada por parâmetro
def matrizTransposta(m):
    transposta = [] # inicializa a lista que receberá a matriz transposta

    for l in range(len(m[0])): # loop que vai de 0 até o tamanho da primera lista lida, representando o tamanho de cada linha da matriz

        linha = [] # inicializa a lista que receberá cada linha da matriz passada, ou seja, cada lista externa da lista de listas

        for c in range(len(m)): # loop que vai de 0 até o tamanho da matriz, ou seja, quantidade de listas que lista possui

            linha.append(m[c][l]) # pega cada item da matriz, ou seja, os itens mais internos da lista, e adiciona ao vetor linha
        transposta.append(linha) # adiciona cada lista gerada acima na variável transposta

    return transposta # retorna a lista transposta representando a matriz transposta

# A funlçao a seguir lê um arquivo de nome informado pelo usuário
def leArquivo(entrada):
    vetor = [] # inicializa o vetor que receberá o conteúdo de cada linha

    with open(entrada+'.txt', 'r') as arquivo: # abre o arquivo informado para leitura, e ao término de seu uso fehca o mesmo

        print(f'\nConteúdo do arquivo {entrada}:')

        linha = arquivo.readline() # recebe a primeira linha do arquivo

        while linha != '': # loop para atualizar o conteúdo de cada linha da lista linha e armazenar seu conteúdo no vetor
            print(linha.strip()) # exibe o conteúdo de cada linha na tela
            vetor.append(linha.split()) # adiciona o conteúdo de cada linha no vetor, separando o conteúdo em listas a cada quebra de linha
            linha = arquivo.readline() # atualiza o conteúdo da variável linha com o conteúdo da próxima linha do arquivo
        print()
    matriz1 = vetor[1:4] # armazena na variável matriz1 a fatia do vetor com o conteúdo lido, do índice 1 ao 3
    matriz2 = vetor[5:] # armazena na variável matriz2 a fatia do vetor com o conteúdo lido, do índice 5 até o final do vetor

    return matriz1, matriz2 # retorna as duas matrizes para o Programa Principal

#Programa Principal
# Informando a funcionalidade do programa ao usuário
print('''
Esse programa recebe o nome de um aquivo de texto 
contento 2 matrizes, e o número de linha de cada de cada 
matriz vindo antes da  matriz relacionada, exibe as matrizes, 
compara, exibe a maior e a sua matriz transposta.
''')

entrada = input('Digite o nome do arquivo a ser lido: ') # recebendo o nome do arquivo a ser lido informado pelo usuário

matriz1, matriz2 = leArquivo(entrada) # ativando a função leArquivo() e recebendo seu retorno nas variáveis matriz1 e matriz2

print('Matriz com mais elementos:')

if matriz1 == []: # Verifica se o retorno da matriz é vazio, o que siginifica que o arquivo não contém conteúdo
    print('Nenhuma matriz foi encontrada no arquivo') # se a condição for verdadeira, informa ao usuário
else: # se a condição for falsa ativa as funções a seguir
    matrizMaior = comparaMatriz(matriz1, matriz2) # função para comparar duas matrizes e retornar a maior
    escreveMatriz(matrizMaior) # chama a função para escrever a matriz maior na tela
print()

print('Transposta da Matriz com mais elementos:')

if matriz1 == []:
    print('Nenhuma matriz foi encontrada no arquivo')
else:
    matrizT = matrizTransposta(matrizMaior) # chama a função que retorna a matriz transposta de uma matriz passada como parêmetro
    escreveMatriz(matrizT) # chama a função para ecrever a matriz transposta na tela

