#APX1-Q2-Acácio Novoa Monteiro - Mat.: 18213050070
#Subprogramas
def leEntrada():
    entrada = input()
    partes = entrada.split()
    lista = []
    for numero in partes:
        lista.append(int(numero))
    return lista
def trocar(vals, posX, posY):
    temp = vals[posX]
    vals[posX] = vals[posY]
    vals[posY] = temp
    return None
def particiona(vals, inicio, fim):
    pivo = vals[inicio]
    i  = inicio+1
    j  = fim
    while i < j:
        while i<fim and vals[i] < pivo:
            i += 1
        while j>inicio and vals[j] >= pivo:
            j -= 1
        if i < j:
            trocar(vals, i, j)
    if pivo>vals[j]:
        trocar(vals, inicio, j)
    return j
def quickSort(vals, inicio, fim):
    if inicio < fim:
        posPivo = particiona(vals,inicio,fim)
        quickSort(vals,inicio,posPivo-1)
        quickSort(vals,posPivo+1,fim)
    return vals
def  ordena (valores):
    vals = quickSort(valores, 0, len(valores)-1)
    return vals
def buscaElemento(lista, num):
    start = 0
    end = len(lista) - 1
    metade = (start + end) // 2
    while (start < end) and (num != lista[metade]):
        if num > lista[metade]:
            start = metade + 1
        else:
            end = metade - 1
        metade = (start + end) // 2
    if num != lista[metade]:
        ind = -1
    else:
        ind = metade
    return ind
def insereElemento(num, lista):
    posicao = 0
    for ind in range(len(lista)):
        if lista[ind] < num:
            posicao = ind + 2
    if num == 1:
        posicao = 1
    print(f'O elemento {num} não consta na lista e, caso deseje, ele será inserido na posição {posicao}')
    decisao = input(f'Você deseja inserir o elemento {num}? Insira S (s) ou N (n):\n ')
    while decisao not in 'SsNn' or decisao == '':
        print('Opção não encontrada!')
        decisao = input(f'Você deseja inserir o elemento {num}? Insira S (s) ou N (n):\n')
    if decisao in 'Nn':
        return lista
    elif decisao in 'Ss':
        lista.append(num)
        ordena(lista)
        return lista
def removeElemento(num, lista, posicao):
    print(f'O elemento {elemento} está na posição {posicao+1}')
    decisao = input(f'Você deseja remover o elemento {elemento}? Insira S (s) ou N (n):\n ')
    while decisao not in 'SsNn':
        print('Opção não encontrada!')
        decisao = input(f'Você deseja remover o elemento {elemento}? Insira S (s) ou N (n):\n')
    if decisao in 'Nn':
        return lista
    elif decisao in 'Ss':
        newList = []
        for n in lista:
            if n != num:
                newList.append(n)
                lista = newList
    return lista
#Programa Principal
numeros = leEntrada()
ordenados = ordena(numeros)
print(f'A lista ordenada é: {ordenados}')
elemento = int(input())
busca = buscaElemento(numeros, elemento)
if busca == -1:
   insereElemento(elemento, numeros)
elif busca >= 0:
    numeros = removeElemento(elemento, numeros, busca)
print(numeros)

