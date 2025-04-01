"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.

"""
from datetime import date
maiores = 0
menores = 0
anoAtual = date.today().year
for c in range(1, 8):
    anoNascimento = int(input("Informe o ano de nascimento: "))
    idade = anoAtual-anoNascimento
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print("Das 6 pessoas {} são maiores.".format(maiores))
print("Das 6 pessoas {} são menores.".format(menores))