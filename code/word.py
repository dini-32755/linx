import os

def main():
    while True:
        opcao = input('Digite 1 para criar um novo arquivo, 2 para abrir um arquivo existente, ou 3 para sair: ')
        if opcao == '1':
            nome_arquivo = input('Digite o nome do arquivo que deseja criar: ')
            criar_arquivo(nome_arquivo)
        elif opcao == '2':
            nome_arquivo = input('Digite o nome do arquivo que deseja abrir: ')
            abrir_arquivo(nome_arquivo)
        elif opcao == '3':
            print('Encerrando o bloco de notas...')
            break
        else:
            print('Opção inválida. Tente novamente.')

def criar_arquivo(nome_arquivo):
    if not nome_arquivo.endswith('.txt'):
        nome_arquivo += '.txt'
    if os.path.exists(nome_arquivo):
        print('O arquivo já existe. Deseja sobrescrevê-lo?')
        confirmacao = input('Digite S para sim ou N para não: ')
        if confirmacao.upper() == 'S':
            arquivo = open(nome_arquivo, 'w')
            escrever_arquivo(arquivo)
        else:
            print('Operação cancelada.')
    else:
        arquivo = open(nome_arquivo, 'w')
        escrever_arquivo(arquivo)

def abrir_arquivo(nome_arquivo):
    if not nome_arquivo.endswith('.txt'):
        nome_arquivo += '.txt'
    if os.path.exists(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        ler_arquivo(arquivo)
    else:
        print('O arquivo não existe.')

def escrever_arquivo(arquivo):
    while True:
        texto = input('Digite o texto que deseja adicionar ao arquivo (ou digite "fim" para encerrar): ')
        if texto == 'fim':
            arquivo.close()
            break
        else:
            arquivo.write(texto + '\n')

def ler_arquivo(arquivo):
    print('Conteúdo do arquivo:\n')
    for linha in arquivo:
        print(linha.rstrip())
    arquivo.close()

if __name__ == '__main__':
    main()
