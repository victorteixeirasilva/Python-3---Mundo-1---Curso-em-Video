"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.

O programa decerá escrever na tela se o usuário venceu ou perdeu.

"""
import random

print("O computador está pensando em um número de 1 a 5...")
numero = random.randrange(1, 6)
numeroSugestão = int(input("Tente adivinhar o número: "))
if numero == numeroSugestão:
    print("Você acertou!")
else:
    print("Você Errou!"
