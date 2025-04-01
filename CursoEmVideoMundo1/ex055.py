"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

"""
maiorPeso = 0.0
menorPeso = 0.0
for c in range(1, 6):
    peso = float(input("Informe o peso: "))
    if peso > maiorPeso:
        maiorPeso = peso
    elif peso < menorPeso or menorPeso == 0.0:
        menorPeso = peso
print("O maior peso informado foi {}Kg".format(maiorPeso))
print("O menor peso informado foi {}Kg".format(menorPeso))