# Crie um programa que leia varios números inteiros pelo teclado.
# O programa só pode parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
qtdDeNumeros = 0
soma = 0
numero = 0
while numero != 999:
    numero = int(input("Informe um número: "))
    qtdDeNumeros += 1
    soma += numero
soma -= numero
qtdDeNumeros -= 1
print("A quantidade de números informados foi {}, e a soma foi {}".format(qtdDeNumeros, soma))
