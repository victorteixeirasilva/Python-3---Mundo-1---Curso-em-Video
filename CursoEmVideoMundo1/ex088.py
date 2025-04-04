"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai
perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo,
cadastrando tudo em uma lista composta. OBS: O número não pode se repetir dentro de um mesmo jogo.

"""
import random
numeroDeJogos = int(input("Informe quantos jogos deseja fazer: "))
jogos = []
for a in range(0, numeroDeJogos):
    jogo = []
    for b in range(1, 7):
        while True:
            numero = random.randrange(1, 61)
            if numero not in jogo:
                break
        jogo.append(numero)
    jogos.append(jogo[:])
    jogo.clear()
print(jogos)