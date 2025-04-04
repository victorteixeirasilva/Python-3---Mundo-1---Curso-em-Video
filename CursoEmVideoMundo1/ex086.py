"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

No final mostre na tela, com a formatação correta.

"""
coluna1 = []
coluna2 = []
coluna3 = []
matriz = [coluna1, coluna2, coluna3]
# matriz = [linhas]
for c in range(0, 3):
    for d in range(0, 3):
        numero = int(input("Informe um número: "))
        matriz[c].append(numero)
for linha in matriz:
    print()
    for numero in linha:
        print(f"|{numero}|", end="")
