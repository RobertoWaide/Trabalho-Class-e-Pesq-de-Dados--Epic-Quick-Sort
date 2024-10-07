def dicktonary(info,games):
    dados = info.split("\n") 
    preco = float((((dados[-1])[2:]).replace(",",".")))
    if preco in games:
        dados.append("")
        dados.extend(games[preco])
    games[preco] = dados
    return games
