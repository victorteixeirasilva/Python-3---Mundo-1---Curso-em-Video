"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde
esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo
que o vencedor tirou o maior número no dado.

"""
import random
import time
import operator
dicionario = {"jogador1":0, "jogador2":0, "jogador3":0, "jogador4":0}
for i in range(0, 4):
    dicionario["jogador{}".format(i)] = random.randrange(1,6)
    print(f"Jogador {i+1}, jogando dado...")
    time.sleep(1)
print(sorted(dicionario.items(), key=operator.itemgetter(1),reverse=True))