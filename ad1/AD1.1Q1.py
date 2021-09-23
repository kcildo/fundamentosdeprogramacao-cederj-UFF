#AD1-1 - Questão 1
#Programa Principal
entrada = input("Digite um número inteiro ou tecle enter para sair: ")
pi = 3.1415
while entrada != "": # loop
    raio = int(entrada)
    if raio %2 != 0:
        perimetro = 2*pi*raio
        area =  pi*raio**2
        print(f"Área e Perímetro do Círculo de Raio  {raio:d} são {area:.2f} e {perimetro:.2f}")
    elif raio %2 == 0:
        print(f"Divisores de {raio:d} são: ", end="")
        for divisao in range(1, raio + 1):
            if raio % divisao == 0:
                print(divisao, end=" ")
        print()
    entrada = input("\nDigite outro número inteiro ou tecle enter para sair: ")


