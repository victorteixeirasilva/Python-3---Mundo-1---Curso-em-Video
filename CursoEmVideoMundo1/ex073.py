# Crie uma tupla preenchida com os primeiros 20 colocados da tabela do Campeonato Brasileiro de Futebol, na ordem
# de colocação, Depois mostre:
#
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em qual posição na tabela está o time da São Paulo.
colocados = ("Desconsiderar", "Fortaleza", "Juventude", "Vasco", "Cruzeiro", "Grêmio", "Bragantino", "Ceará", "Corinthians", "Flamengo", "Internacional", "Bahia", "São Paulo", "Sport", "Botafogo", "Palmeiras", "Atlético-MG", "Santos", "Mirassol", "Fluminense", "Vitória")
print()
print("_" * 63)
print("|{:^61}|".format("Os 5 primeiros colocados!"))
print("_" * 63)
print("|{:^30}|{:^30}|".format("Colocação", "Time"))
print("_" * 63)
for c in range(1, 6):
    print("|{:^30}|{:^30}|".format(c, colocados[c]))
print("_" * 63)
print()
print("_" * 63)
print("|{:^61}|".format("Os últimos 4 colocados da tabela!"))
print("_" * 63)
print("|{:^30}|{:^30}|".format("Colocação", "Time"))
print("_" * 63)
for c in range(20, 16, -1):
    print("|{:^30}|{:^30}|".format(c, colocados[c]))
print("_" * 63)
print()
print("Lista de times, ordem alfabetica ({})".format(sorted(colocados)))
print()
print(colocados.index("São Paulo"))

