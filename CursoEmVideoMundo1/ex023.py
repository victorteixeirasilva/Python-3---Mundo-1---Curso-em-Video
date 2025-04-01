"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

Ex:
Digite um número: 1834

unidade: 4
dezena: 3
centena: 8
milhar: 1
"""

numero = input("Informe um número de 0 a 9999: ")
unidade = numero[3]
dezena = numero[2]
centena = numero[1]
milhar = numero[0]
print("Unidade: ", unidade)
print("Dezena: ", dezena)
print("Centena: ", centena)
print("Milhar: ", milhar)
