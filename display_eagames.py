def display(games,preco):
    for i in preco:
        game = games.get(i)
        for j in game:
            print(j)
        print("")
    input("Aperte Enter para voltar...")

def jogo_velho(games):
    for game in games.values():
        for info in game:
            print(info)
        print("")
    input("Aperte Enter para voltar...")