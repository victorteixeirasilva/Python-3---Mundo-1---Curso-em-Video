# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
import random
numeros = (random.randint(1, 11), random.randint(1,11), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print(numeros)
maiorNumero = 0
menorNumero = 0
for c in numeros:
    if c >= maiorNumero:
        maiorNumero = c
    elif c < menorNumero:
        menorNumero = c
    if menorNumero == 0:
        menorNumero = c
print(f"Menor número da tupla {menorNumero}")
print(f"Maior número da tupla {maiorNumero}")