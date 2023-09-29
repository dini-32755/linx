import time, sys, os
import pyfiglet as pyg
from time import sleep
from rich.table import *
from rich.box import *
from rich.progress import *
from rich.terminal_theme import *
from rich.live import *
from rich.panel import *
res= pyg.figlet_format("Welcome to Linx RPG!", font = "bloody")   
print(res)



player_name = str(input('character name:'))
table = Table(title='character '+ player_name)


table.add_column("status", style="cyan", no_wrap=True)
table.add_column("status level", style="magenta")
table.add_row('vida inicial', '110')
table.add_row('magia', '200')
table.add_row('cerebro', '90')

console = Console()
console.print(table, justify="center")


while 1 == 1:
    d1 = str(input('queres fazer o tuturial ,Y or N :'))
    if d1 == 'y' or 'Y':
        print('ok, vamos lá para a tua primeira luta\n')
        break
    else:
        print('denovo')


table = Table(title='action')
table.add_column("keyboard", style="blue" )
table.add_column("1", style="green" )
table.add_column("2", style="green" )
table.add_column("3", style="green" )
table.add_row('action', "espada:25 dm", 'defesa')#'feiticos'
console = Console()
console.print(table, justify="botton")
vida_do_personagem = int(110)
dano_do_personagem = int(25)
vida_do_goblin = int(30) 
dano_do_goblin = int(20)
print('''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣝⠛⠿⢿⣿⣿⣿⡀⠘⠻⢶⣄⡀⠀⠀⢀⣠⡶⠟⠃⢀⣿⣿⣿⣿⠿⠛⣫⣿
⣿⣿⣷⡄⠀⠉⣿⠈⣿⣶⣤⣀⣉⢋⡀⢀⡙⣉⣀⣤⣶⣿⠁⣿⠉⠀⢠⣾⣿⣿
⣿⣿⣿⣿⣄⠀⢹⣧⢸⣧⣈⣟⣙⣿⠁⠈⣿⣋⣻⣁⣼⡇⣼⡏⠀⣠⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣴⡟⠁⠚⠋⠉⠉⠹⣧⠀⠀⣼⠏⠉⠉⠙⠓⠈⢻⣦⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡴⣤⣄⣀⠀⣠⡆⠹⣇⣸⠏⢰⣄⠀⣀⣠⣤⢦⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⡘⢿⣟⣻⣿⣷⣤⣿⣿⣤⣾⣿⣟⣻⡿⢃⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⡄⠙⢿⣼⣿⠀⢹⡏⠀⣿⣧⡿⠋⢠⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠙⢿⣧⣸⣇⣼⡿⠋⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠈⠻⠟⠁⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
vida do goblin :30
dano do goblin :20
''')
while vida_do_goblin > 0:

    acao = input('O que vais fazer:')
               
    if acao == 1:
        n3 = vida_do_goblin - dano_do_personagem
        vida_do_goblin_1 = n3
        print(n3) 
        if n3 <= 0:
            print('''goblin morto
+30 xp\n''')
    elif acao == 2:
        print('defesa NVL.1 ativada')
        n4 = vida_do_personagem - (dano_do_goblin / 1.5)
        print(n4)
        vida_do_personagem = n4


    if vida_do_goblin <= 0:
        break