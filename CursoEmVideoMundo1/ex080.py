# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o short()).
#
# No final, mostre a lista ordenada na tela.
numeros = []
for c in range(1, 6):
    numero = int(input("Informe um número: "))
    if len(numeros) == 0:
        numeros.append(numero)
    else:
        for i, c in enumerate(numeros):
            if numero < c and numero not in numeros:
                numeros.insert(i, numero)
            elif numero > c and numero not in numeros:
                numeros.append(numero)
print("-=-" * 20)
print(numeros)