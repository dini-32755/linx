# linx
system pi linx

made by Dinis py
made for raspberrypi



Start
|
|--- Print "run-user1╰(*°▽°*)╯"
|--- Print "user1 startup..."
|--- Sleep for 3 seconds
|--- Print "startup successful"
|--- Print "Welcome to Linx!"
| 
|--- While True:
|     |
|     |--- Get user input as action1
|     |
|     |--- If action1 == '--help':
|     |     |--- Print help menu
|     |
|     |--- Elif action1 == '--pc-off':
|     |     |--- Print "turning off the pc..."
|     |     |--- Sleep for 2 seconds
|     |     |--- Exit the program
|     |
|     |--- Elif action1 == '--calculator':
|     |     |--- Get user input as action2
|     |     |
|     |     |--- If action2 == '+':
|     |     |     |--- Get two numbers, add them, and print the result
|     |     |
|     |     |--- Elif action2 == '-':
|     |     |     |--- Get two numbers, subtract them, and print the result
|     |     |
|     |     |--- Elif action2 == '*':
|     |     |     |--- Get two numbers, multiply them, and print the result
|     |     |
|     |     |--- Elif action2 == '/':
|     |     |     |--- Get two numbers, divide them, and print the result
|     |
|     |--- Elif action1 == '--notepad':
|     |     |--- Display notepad options:
|     |     |--- While True:
|     |     |     |
|     |     |     |--- Get user option as opcao
|     |     |     |
|     |     |     |--- If opcao == '1':
|     |     |     |     |--- Get a filename and create a new file
|     |     |     |     |
|     |     |     |--- Elif opcao == '2':
|     |     |     |     |--- Get a filename and open an existing file
|     |     |     |     |
|     |     |     |--- Elif opcao == '3':
|     |     |     |     |--- Print "Encerrando o bloco de notas..."
|     |     |     |     |--- Break the loop
|     |     |     |     
|     |     |     |--- Else:
|     |     |     |     |--- Print "Opção inválida. Tente novamente."
|     |
|     |--- Elif action1 == '--explore':
|     |     |--- List files in the current directory and print them
|     |
|     |--- Elif action1 == '--hacking-tool':
|     |     |--- Print "Linx hacking tool!" banner
|     |     |--- Create job progress bar for various hacking tasks
|     |     |--- Create an overall progress bar
|     |     |--- Update progress bars until finished
|     |
|     |--- Elif action1 == '--office--tool/excel':
|     |     |--- Get user input for table title and data
|     |     |--- Create a table with specified columns and data
|     |     |--- Print the table
|     |
|     |--- Elif action1 == '':
|     |     |--- Print a blank line
|     |
|     |--- Else:
|     |     |--- Print "error"
|
End
