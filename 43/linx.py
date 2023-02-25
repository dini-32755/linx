import time, sys, os                                                                                                                                                                                                                                                                                          
#print('boas bem vindo a este site')

print('\033[32mrun-user1╰(*°▽°*)╯\033[m')

while True:
    password = str(input('\033[32mpass§user1 - \033[m''\033[1;35m$ \033[m'))
    f = open("password.txt", "r")
    if password == f.readline():
        break

print('\033[32muser1 startup...\033[m')
time.sleep(3)
print('\033[32mstartup succesefull\033[m')


while 1 == 1:
    action1 = str(input('\033[32muser1 - \033[m''\033[1;35m$ \033[m'))

    if action1 == '--help':
        print('''-----------------------------------------
     ᓚᘏᗢ       Commands  (ˉ﹃ˉ)           
-----------------------------------------
--notepad       open the note pad;
--help      if you need help 
--help-advanced    more help    
--calculator    it's a calculator ¯\_(ツ)_/¯
--explore
--reset-password
--pc-off   turn off computer;

-------------------------------------''')
    elif action1 == '--pc-off':
        print('\033[1;31mturning off the pc...\033[m')
        time.sleep(2)
        sys.exit()

    elif action1 == '--calculator':
        action2 = str(input('\033[32mcalc§user1 - \033[m''\033[1;35m$ \033[m'))

        if action2 == '+':
           x = float(input('\033[32mcalc§user1@+ - \033[m''\033[1;35m$ \033[m'))
           y = float(input('\033[32mcalc§user1@+ - \033[m''\033[1;35m$ \033[m'))
           z = x + y
           print(z)

        elif action2 == '-':
           x = float(input('\033[32mcalc§user1@- - \033[m''\033[1;35m$ \033[m'))
           y = float(input('\033[32mcalc§user1@- - \033[m''\033[1;35m$ \033[m'))
           z = x - y
           print(z)

        elif action2 == '*':
           x = float(input('\033[32mcalc§user1@* - \033[m''\033[1;35m$ \033[m'))
           y = float(input('\033[32mcalc§user1@* - \033[m''\033[1;35m$ \033[m'))
           z = x * y
           print(z)

        elif action2 == '/':
           x = float(input('\033[32mcalc§user1@/ - \033[m''\033[1;35m$ \033[m'))
           y = float(input('\033[32mcalc§user1@/ - \033[m''\033[1;35m$ \033[m'))
           z = x / y
           print(z)

    elif action1 == '--notepad':
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
    elif action1 == '--explore':
        for file in os.listdir():
            if os.path.isfile(file):
                print(file)
       
    else:
        print('\033[1;31merror\033[m')
        
                                    
