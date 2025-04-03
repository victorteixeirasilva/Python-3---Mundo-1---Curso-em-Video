# Crie um programa que leia dois valores e mostre um menu na tela:
#
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.
opcao = 0
numeroUm = 0
numeroDois = 0
while opcao != 5:
    opcao = 4
    while opcao == 4:
        numeroUm = float(input("Informe um número: "))
        numeroDois = float(input("Informe outro número: "))
        opcao = 0
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos números")
    print("[5] Sair do programa")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("A soma de {} + {} = {}".format(numeroUm, numeroDois, numeroUm+numeroDois))
    elif opcao == 2:
        print("A multiplicação de {} x {} = {}".format(numeroUm, numeroDois, numeroUm*numeroDois))
    elif opcao == 3:
        if numeroUm > numeroDois:
            print("O maior número informado foi {}".format(numeroUm))
        else:
            print("O maior número informado foi {}".format(numeroDois))
