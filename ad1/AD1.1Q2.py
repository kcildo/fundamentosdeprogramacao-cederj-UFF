# Programa Principal
cont = soma = media = maior = menor = 0

qtdEntrada = int(input("Digite a quantide de números a serem lidos: "))
while qtdEntrada < 1:
    print('Nâo digitou número válido, por favor digite um número maior que [0]')
    qtdEntrada = int(input("Digite a quantide de números a serem lidos: "))

print(f'Digite os {qtdEntrada} números, a cada número tecle [ENTER]: ')

while cont < qtdEntrada:
    entrada = int(input())
    soma = soma + entrada
    cont += 1
    if cont == 1:
        maior = menor = entrada
    elif entrada > maior:
        maior = entrada
    elif entrada < menor:
        menor = entrada

media = soma / qtdEntrada
print(f'''\nSoma: {soma:d}
Média: {media:.2f}
Menor: {menor:d}
Maior: {maior:d}''')





