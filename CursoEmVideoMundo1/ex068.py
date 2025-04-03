# Faça um programa que jogue par ou ímpar com o computador. O jogo só sera interrompido quando o jogador PERDER,
# Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
totalDeVitórias = 0
while True:
    nJogador = int(input("Informe um número: "))
    nComputador = random.randrange(1, 11)
    soma = nJogador + nComputador
    opção = ""
    while opção != "I" and opção != "P":
        opção = str(input("Você quer impar ou par [I/P]: ")).strip().upper()
    if opção == "I":
        if (soma % 2) == 0:
            print("Você perdeu! A soma dos número escolhidos foi {}".format(soma))
            break
    elif opção == "P":
        if not (soma % 2) == 0:
            print("Você perdeu! A soma dos número escolhidos foi {}".format(soma))
            break
    opção = ""
    print("Você venceu!, A soma dos número escolhidos foi {}".format(soma))
    totalDeVitórias +=1
print(f"Você venceu {totalDeVitórias} consecutivas!")