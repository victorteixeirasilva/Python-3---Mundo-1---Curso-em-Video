# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. o programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.
contadorDeNumeros = 0
somaDosNumeros = 0
continuar = True
maiorNumero = 0
numero = 0
menorNumero = numero
while continuar:
    contadorDeNumeros += 1
    numero = int(input("Informe um número: "))
    somaDosNumeros += numero
    if numero > maiorNumero:
        maiorNumero = numero
    elif numero < menorNumero or numero == 0:
        menorNumero = numero
    opcao = 'vi'
    while opcao.upper() != 'S' and opcao.upper() != 'N':
        opcao = input("Deseja continuar [S/N]: ")
        if opcao.upper() == 'N':
            continuar = False
        elif opcao.upper() != 'N' and opcao.upper() != 'S':
            print("Opção inválida! ")
print("Foram digitados {} números, a soma dos números é {}.".format(contadorDeNumeros, somaDosNumeros))