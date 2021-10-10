#APX1-Q1-Acácio Novoa Monteiro - Mat.: 18213050070
#Subprogramas
def escreveTupla(linha):
    return tuple(map(int, linha.split()))
def lerPontos():
    coord = []
    linha = input()
    while linha != '':
        ponto = escreveTupla(linha)
        coord.append(ponto)
        linha = input()
    return coord
def calcula(pontos):
    circulo = pontos[0]
    xC, yC, rC = circulo
    cont = 0
    for lin in range(1, len(pontos)):
        xP, yP = pontos[lin]
        resultado = ((xP - xC)**2 + (yP - yC)**2)**0.5
        if resultado <= rC:
            print(f'{pontos[lin]} Está dentro do círculo {circulo}')
            cont += 1
    return cont
#Programa Principal
print('''Digite inicialmente 3 inteiros separados por espaço representando as coordenadas de um círculo em 
seguida digite [ENTER], posteriormente digite 2 inteiros separados por espaço representando coordenadas
quaisquer ao final digite [ENTER], quando quiser encerrar as entradas de 2 coordenadas deixe uma linha vazia 
e digite [ENTER]!
''')
pontos = lerPontos()
cont = calcula(pontos)
percent = round(cont/(len(pontos)-1)*100, 1)
print(f'Quantidade de Pontos Processados: {len(pontos)-1}')
print(f'Quantidade de Pontos Dentro de Círculo: {cont}')
print(f'Percentual de Pontos Dentro: {percent}%')
