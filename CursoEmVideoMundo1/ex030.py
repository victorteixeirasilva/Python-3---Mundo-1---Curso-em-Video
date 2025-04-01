"""
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar

"""
numero = int(input("Informe um número inteiro: "))
if (numero%2)==0:
    print("O número {}, é PAR!".format(numero))
else:
    print("O número {}, é IMPAR!".format(numero))