"""
Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.

B) A soma dos valores da terceira coluna.

C) O maior valor da segunda linha.

"""
coluna1 = []
coluna2 = []
coluna3 = []
matriz = [coluna1, coluna2, coluna3]
totSoma = 0
totColuna3 = 0
maiorSegundaLinha = 0
for c in range(0, 3):
    for d in range(0, 3):
        numero = int(input("Informe um número: "))
        matriz[c].append(numero)
        totSoma += numero
        if d == 2:
            totColuna3 += numero
        if c == 1:
            if maiorSegundaLinha < numero or maiorSegundaLinha == 0:
                maiorSegundaLinha = numero
for linha in matriz:
    print()
    for numero in linha:
        print(f"|{numero}|", end="")
print()
print(f"A soma de todos os valores é {totSoma}")
print(f"A soma dos números da terceira coluna é {totColuna3}")
print(f"O maior valor da segunda linha é {maiorSegundaLinha}")