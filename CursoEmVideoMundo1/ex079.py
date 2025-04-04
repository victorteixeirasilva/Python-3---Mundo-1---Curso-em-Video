# Crie um programa onde o usuário pode digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o númerico já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
# valores únicos digitados, em ordem crescente.
numeros = []
while True:
    numero = int(input("Informe um número: "))
    if numero not in numeros:
        numeros.append(numero)
    else:
        print("Número já adicionado, não vou adicionar")
    while True:
        desejaContinuar = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
        if desejaContinuar == "S" or desejaContinuar == "N":
            break
    if desejaContinuar == "N":
        break
print(sorted(numeros))