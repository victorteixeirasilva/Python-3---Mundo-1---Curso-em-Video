# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

import random

print("O computador está pensando em um número de 1 a 5...")
numero = random.randrange(1, 11)
qtdPalpites = 1
jogoContinua = True
while jogoContinua:
    numeroSugestão = int(input("Tente adivinhar o número: "))
    if numero == numeroSugestão:
        print("Você acertou!, e deu {} palpites".format(qtdPalpites))
        jogoContinua = False
    else:
        print("Você Errou!")
        qtdPalpites += 1

