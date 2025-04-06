"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
dicionário, incluindo o total de gols feitos durante o campeonato.

"""
jogador = dict()
jogador["nome"] = input("Informe o nome do jogador: ")
quantidadeDePartidaJogadas = int(input("Informe a quantidade de partida jogadas: "))
partidas = []
for i in range(0, quantidadeDePartidaJogadas):
    partidas.append(int(input(f"Informe a quantidade de gols feitos na partida {i}: ")))
totGols = 0
for i, p in enumerate(partidas):
    totGols += p
jogador["partidas"] = partidas
jogador["total de gols"] = totGols
print(jogador)