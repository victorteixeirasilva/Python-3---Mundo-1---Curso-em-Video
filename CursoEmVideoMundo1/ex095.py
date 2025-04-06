"""
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema
de visualização de detalhes do aproveitamento de cada jogador.

Retorno:
---
[Tabela em formato tabular de cada jogador]
---
Deseja ver detalhes de algum jogador [S/N]: s
Mostrar dados de qual jogador?
--- Levantamento do jogador {nome} ---
    No jogo x fez n gols.
    No jogo y fez n gols.
    ...
---
Deseja ver detalhes de algum jogador [S/N]: n
Encerrando...
"""
import time
jogadores = list()
while True:
    jogador = dict()
    jogador["nome"] = input("Informe o nome do jogador: ")
    quantidadeDePartidaJogadas = int(input("Informe a quantidade de partida jogadas: "))
    partidas = []
    for i in range(0, quantidadeDePartidaJogadas):
        partidas.append(int(input(f"Informe a quantidade de gols feitos na partida {i}: ")))
    totGols = 0
    for i, p in enumerate(partidas):
        totGols += p
    jogador["partidas"] = partidas.copy()
    jogador["total de gols"] = totGols
    jogadores.append(jogador.copy())
    jogador.clear()
    while True:
        r = input("Deseja adicionar outro jogador [S/N]: ").strip().upper()[0]
        if r == "":
            r = "D"
        if r in "SN":
            break
    if r == "N":
        break
print(f"{"-"*79}")
print(f"|{"cod":^25}|{"Jogador":^25}|{"total de gols":^25}|")
print(f"{"-"*79}")
for i,j in enumerate(jogadores):
    print(f"|{i:^25}|{j["nome"]:^25}|{j['total de gols']:^25}|")
print(f"{"-"*79}")
while True:
    while True:
        r = input("Deseja ver detalhes de algum jogador [S/N]: ").strip().upper()[0]
        if r == "":
            r = "d"
        if r in "SN":
            break
    if r == "S":
        cod = int(input("Mostrar dados de qual jogador (cod)? "))
        print(f"{"-" * 105}")
        print(f"|{"cod":^25}|{"Jogador":^25}|{"Partida":^25}|{"Gols":^25}|")
        print(f"{"-" * 105}")
        for i, j in enumerate(jogadores):
            if i == cod:
                for n, partida in enumerate(j["partidas"]):
                    print(f"|{cod:^25}|{j["nome"]:^25}|{n:^25}|{partida:^25}|")
        print(f"{"-" * 105}")
    else:
        print("Encerrando...")
        time.sleep(2)
        break