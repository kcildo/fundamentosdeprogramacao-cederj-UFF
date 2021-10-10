#APX1-Q3b-Acácio Novoa Monteiro - Mat.: 18213050070
#Programa Principal sem recursividade
n = int(input())
ano1 = float(input())
ano2 = float(input())
resultados = [ano1, ano2]
for i in range(0, n-2):
    anoN = (resultados[i+1] * 2) - (resultados[i] / 2)
    resultados.append(anoN)
print(f'''No ano 1 há {resultados[0]} flores e no ano 2, {resultados[1]} flores.
Assim, no ano {n} há {resultados[n-1]:.2f} flores.''')

