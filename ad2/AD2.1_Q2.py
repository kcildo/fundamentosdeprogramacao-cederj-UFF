#AD2-1 - Questão 2 - Acácio Novoa Monteiro - 18213050070
#Subprogramas
import os # importanto a biblioteca 'os', utilizada para manipulação de
          # arquivos. Usada nesse programa somente para deletar o arquivo temporário

def leArquivo(nomeArquivo): # Função para exibir o conteúdo do arquivo na tela

    with open(nomeArquivo + '.txt', 'r', encoding='utf-8') as arquivo: # método para abrir e fechar o arquivo após a leitura.

        linha = arquivo.readline() # recebendo a primeira linha do arquivo
        while linha != '': # loop para exibir a linha na tela, atualizar a variável linha e exbiri o novo conteúdo da mesma
            print(linha.strip())
            linha = arquivo.readline() # atualiza o conteúdo da variável linha, até uma linha vazia ser encontrada
        print()

    return None

# A função a seguir le linha por linha do arquivo, procura as palavras informadas na linha
# remove e salva num arquivo temporário, ao final seu retorno chama a função atualizaArquivo()
# para atualizar o conteúdo do arquivo informado e posteriormente apaga o arquivo temporário
def removePalavras(palavras, nomeArquivo):

    palavras = palavras.split() # recebe a linha de palavras informadas par remoção em uma lista, onde cada palavra é um item da lista

    with open(nomeArquivo + '.txt', 'r', encoding='utf-8') as arquivo: # abrindo arquivo informado pelo usuário para leitura

        with open('temporario.txt', 'w', encoding='utf-8') as arqTemp: # criando arquivo temporário para escrita

            linha = arquivo.readline() # lendo a primeira linha do arquivo informado pelo usuário
            while linha != '': # looping para atualizar e lê as proximas linhas
                partes = linha.split() # recebendo o conteúdo atual da variável linha numa lista
                partes.append('\n') # adicionando uma quebra de linha ao final do conteúdo da linha

                for ind in range(len(palavras)): # iterando sobre a lista de palavras
                    if palavras[ind] in partes: # identificando as palavras dentro da lista com o conteúdo da linha lida
                        partes.remove(palavras[ind]) # removendo da lista de conteúdo das linhas lidas as palavras encontradas

                for palavra in partes: # iterando na lista com o conteúdo das linhas já com as palavras informadas removidas
                    arqTemp.write(palavra + ' ') # escrevendo o conteúdo no arquivo temporário

                linha = arquivo.readline() # atualizando o conteúdo da linha lida do arquivo informado pelo usuário

    return atualizaArquivo(nomeArquivo) # retorno chamando a função atualizaArquivo()

# A função a seguir escreve o conetúdo do arquivo temporário no arquivo
# informado pelo usuário atualizando assim o conteúdo do arquivo informado.
def atualizaArquivo(nomeDest):

    with open('temporario.txt', 'r', encoding='utf-8') as arqOrig: # abrindo o arquivo temporário

        with open(nomeDest + '.txt', 'w', encoding='utf-8') as arqDest: # abrindo o arquivo informado pelo usuário

            for linha in arqOrig: # iterando sobre a cada linha do arquivo temporário
                arqDest.write(linha) # escrevendo o conteúdo de cada linha do arquivo temporário no arquivo informado pelo usuário

    os.remove('temporario.txt') # deletando o arquivo temporário

    return None

#Programa Principal
print('''
Esse programa remove algumas palavras informadas de um arquivo texto informado

Digite as palavras a serem eliminadas do arquivo texto, 
todas na mesma linha separadas por espaço: ''') # informando ao usuário a funcionalidade do programa

eliminadas = input() # recebendo linha com as palavras a serem removidas

texto = input('Digite o nome do arquivo a ser lido:\n') # recebendo o nome do arquivo a ser lido

print(f'\nConteúdo do arquivo {texto}:\n')
leArquivo(texto) # ativando a função leArquivo, o qual mostra o conteúdo do arquivo na tela

print(f'Novo Conteúdo do arquivo {texto}:\n')
removePalavras(eliminadas, texto) # ativando a função removePalavras, a mesma removerá as palavras passadas
leArquivo(texto) # chamando a função leArquivo novamente para exibir o novo conteúdo do arquivo informado.
