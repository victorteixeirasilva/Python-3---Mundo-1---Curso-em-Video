"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado
for ímpar, desconsidere-o.

"""
for n in range(1, 7):
    number = int(input("Informe um número: "))
    if (number % 2) == 0:
        print(number)