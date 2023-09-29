import time, sys, os
import pyfiglet as pyg
from time import sleep
from rich.table import *
from rich.box import *
from rich.progress import *
from rich.terminal_theme import *
from rich.live import *
from rich.panel import *

print('\033[32mrun-user1╰(*°▽°*)╯\033[m')
#    while True:
#        password = str(input('\033[32mpass§user1 - \033[m''\033[1;35m$ \033[m'))
#      f = open('password.txt', "r")
#      if password == f.readline():
#       break
print('\033[32muser1 startup...\033[m')
time.sleep(3)
print('\033[32mstartup succesefull\033[m')

res= pyg.figlet_format("Welcome to Linx!", font = "speed")   
print(res)

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
--hacking-tool
--office--tool/excel
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
        res= pyg.figlet_format("Notepad!", font = "slant")   
        print(res)
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
    elif action1 == '--hacking-tool':
        res= pyg.figlet_format("Linx hacking tool!   😁  （；´д｀）ゞ", font = "bloody")   
        print(res)
        job_progress = Progress(
            "{task.description}",
            SpinnerColumn(),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        )
        job1 = job_progress.add_task("[green]mac adress")
        job2 = job_progress.add_task("[magenta]ip adress", total=200)
        job3 = job_progress.add_task("[cyan]subnetmask", total=150)

        total = sum(task.total for task in job_progress.tasks)
        overall_progress = Progress()
        overall_task = overall_progress.add_task("All Jobs", total=int(total))

        progress_table = Table.grid()
        progress_table.add_row(
            Panel.fit(
                overall_progress, title="Overall Progress", border_style="green", padding=(2, 2)
            ), Panel.fit(job_progress, title="[b]Linx hacking tools", border_style="red", padding=(1, 2)),
        )

        with Live(progress_table, refresh_per_second=10):
            while not overall_progress.finished:
                sleep(0.1)
                for job in job_progress.tasks:
                    if not job.finished:
                        job_progress.advance(job.id)

                completed = sum(task.completed for task in job_progress.tasks)
                overall_progress.update(overall_task, completed=completed)
    elif action1 == '--office--tool/excel':

        v4 = str(input(''))
        table = Table(title=v4)


        n3 = str(input(''))
        n2 = str(input(''))
        n1 = str(input(''))
        table.add_column("User", style="cyan", no_wrap=True)
        table.add_column("Email", style="magenta")
        table.add_column("password", justify="right", style="green")

        table.add_row(n3, n2, n1)
        table.add_row("Tiago salgado", "9545@ebaveromar.com", "*******")
#        table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
#        table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

        console = Console()
        console.print(table, justify="left")
    elif action1 == '':
        print('')
    else: 
        print('error')