"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os numa lista única
que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

"""
par = []
impar = []
numeros = [par, impar]
for c in range(1, 8):
    numero = int(input("Informe um número: "))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
print(numeros)
numeros[0].sort()
numeros[1].sort()
print(numeros[0])
print(numeros[1])