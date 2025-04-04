# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
numeros = []
for i in range(1, 6):
    numeros.append(int(input("Informe um número: ")))
listaAjustada = sorted(numeros)
print(f"O menor número informado foi {listaAjustada[0]}, e está na posição 0")
print(f"O maior número informado foi {listaAjustada[len(listaAjustada)-1]}, e está na posição {len(listaAjustada)-1}")
