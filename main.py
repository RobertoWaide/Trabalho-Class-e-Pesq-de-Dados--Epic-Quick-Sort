import time
import os

import pega_jogos
import quicksort
import display_eagames


def main ():
    while True:
        try:
            print ("""Best Seller da Epic Games\n
--Escolha as opções para realizar a pesquisa--\n               
1- Receber os dados da Epic Games.
2- Organizar os dados. 
3- Visualizar os dados não organizados.
4- Visualizar os dados organizados.""")

            opc = input("Selecione a opção: ")
            
            if opc == "1":
                games = pega_jogos.web()
            elif opc == "2":
                listaganizada = quicksort.quicksort(list(games.keys()))
                print("Lista Organizada")
                time.sleep(2)
            elif opc == "3":
                display_eagames.jogo_velho(games)
            elif opc == "4":
                os.system('cls')
                display_eagames.display(games,listaganizada)
            os.system('cls')
    
        except UnboundLocalError:
            os.system('cls')
            print(f"Recaba os dados primeiro e depois organize-os\n")
        
        except BaseException as error:
            os.system('cls')
            print(error)

        
        
main()