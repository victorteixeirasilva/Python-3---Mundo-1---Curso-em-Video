# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
# 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles.
# (desconsiderando o flag).
qtdDigitados = 0
soma = 0
while True:
    numero = int(input("Informe um número: "))
    if numero == 999:
        break
    qtdDigitados += 1
    soma += numero
print(f"Forám digitados {qtdDigitados} números, e a soma entre eles foi {soma}.")