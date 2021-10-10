#Subprogramas
# Função para retornar um vetor de números repetidos dentro do vetor original
def elementoRepetido(numeros):
    # criando um vetor recebendo os valores do vetor original sem repetições utilizando o método set
    numerosUnicos = set(numeros)
    # adicionando os elementos repetidos no vetor que será retornado utilizando list comprehensions
    numRepetidos = [n for n in numerosUnicos if numeros.count(n)>1]
    return numRepetidos # retornado o vetor resultado

# Função para retornar um vetor com a ordem decrescente do vetor original
def invertVetor(numeros):
    vetorInvertido = []
    # iterando sobre o vetor original de maneira decrescente e adicionando os elementos lidos ao inverso no vetor resultado
    for n in range(len(numeros)-1, -1, -1):
        vetorInvertido.append(numeros[n])
    for ind in vetorInvertido:
        # imprimindo na saída padrão elemento por elemento na mesma linha de forma que não apareçam [] e ,
        print(ind, end=' ')
    return vetorInvertido # retornando o vetor invertido

# Função para descobrir as posições do maior e menor elemento dentro do vetor e as posições que teriam que ser realizadas as
#  trocas para que o vetor fosse ordenado de maneira crescente, como resultado será retornado um vetor indicando as posições de troca
def descobrePosicoes(numeros):
    posicoes = []
    cont = 0
    for i in range(len(numeros)-1): # iterando no vetor original
        for j in range(i+1, len(numeros)): # iterando da posição i+1 até o final do vetor original
# Onde os elementos na posição i for > os elementos na posição j será atualizado o valor da posição inicial
# e adicionado o número do índice i e j no vetor que conterá as referências de posições para o usário final
# saber aonde seria realizada as trocas
            if int(numeros[i]) > int(numeros[j]):
                posicoes.append((i+1, j+1))
                cont +=1
    return posicoes, cont # retornando o vetor com as posições e as quantidades de trocas que deveriam ser realizadas

# Função para gerar um novo vetor contendo a diferença entre o vetor original e o vetor invertido
def diferencaDeVetores(numeros, numInvert):
    vetorDiferenca = []
    for n in range(len(numeros)):
        vetorDiferenca.append(int(numeros[n]) - int(numInvert[n]))
    return vetorDiferenca # retornando o vetor com a diferença
# Progama Principal
entrada = input('Digite números inteiros separados por espaço ao final tecle [ENTER]: \n') # recebendo valores inteiros da entrada padrão
numeros = (entrada).split() # tansformando a entrada em uma lista e guardando em uma variável
numRepetidos = elementoRepetido(numeros) # chamando a função elementoRepetido e guardando o retorno em uma variável
posicoes, qtdInversoes = descobrePosicoes(numeros) # chamando a função descobrePosicoes e guardando as variáveis retornadas

#imprimindo na saída padrão o resultado de cada subprogramção(função)
print('Os elementos que se repetem são: {}'.format(numRepetidos))
print('Há {} inversões, e as posições são: {}'.format(qtdInversoes, posicoes))
print('Sequência inversa: ', end='')
# chamando a função ivertVetor onde a mesma já imprime o resultado na saída padrão e retorna o vetor para ser armazenado
numInvert = invertVetor(numeros)
print('\nA sequência obtida da diferença é: {}'.format(diferencaDeVetores(numeros, numInvert)))
