#APX1-Q2-Acácio Novoa Monteiro - Mat.: 18213050070
#Subprogramas
def leEntrada(qtd):
    linhas = []
    cont = 0
    print(f'Digite seu texto com {qtd} linhas: ')
    while cont < qtd:
        linha = input()
        partes = linha.upper().split()
        for palavra in partes:
            linhas.append(palavra)
        cont += 1
    # if linhas == []:
    #     print('Nenhuma palavra foi lida!')
    #     return None
    return linhas
def palavrasRepetidas(palavras):
    listaRepetidas = []
    qtd = 1
    for lin in range(len(palavras)-1):
        for palavra in palavras:
            if (palavras.count(palavra) > palavras.count(palavras[lin+1])) and (palavra not in listaRepetidas):
                listaRepetidas.append(palavra)
                qtd += 1
    return listaRepetidas, qtd
def escrevePalavras(palavras):
    for palavra in palavras:
        print(palavra)
#Programa Principal
qtdentrada = int(input('Digite a quantidade de linhas de texto a ser escrito: '))
frases = leEntrada(qtdentrada)
if frases == []:
    print('Nenhuma palavra foi lida!')
else:
    repetidas, qtdRepeat = palavrasRepetidas(frases)
    escrevePalavras(repetidas)
    print(f'Ocorreu(ram) {qtdRepeat} vez(es).')
