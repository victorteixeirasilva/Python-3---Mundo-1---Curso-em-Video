"""
Crie um programa que faça o computador jogar Jokenpô com você.

"""
import random
computador = random.randrange(1, 4)
print("Escolha uma opção")
print("1 - Para Pedra.")
print("2 - Para Papel.")
print("3 - Para Tesoura.")
jogador = int(input("Escolha: "))
if (jogador == 1 and computador == 1) or (jogador == 2 and computador == 2) or (jogador == 3 and computador == 3):
    print("Jogo empatado!")
elif (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2):
    print("Jogador Venceu!")
elif (computador == 1 and jogador == 3) or (computador == 2 and jogador == 1) or (computador == 3 and jogador == 2):
    print("Computador Venceu!")