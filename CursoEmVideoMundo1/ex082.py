# Crie um programa que vai ler vários números e colocar em uma lista.
#
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores impares digitados, respectivamente.
#
# Ao final, mostre o conteúdo das três listas geradas.
numeros = []
numerosPares = []
numerosImpares = []
while True:
    numero = int(input("Informe um número: "))
    numeros.append(numero)
    while True:
        r = str(input("Deseja continuar [S/N]")).strip().upper()[0]
        if r in "SN":
            break
    if r in "N":
        break
for n in numeros:
    if (n % 2) == 0:
        numerosPares.append(n)
    else:
        numerosImpares.append(n)
print("-=-" * 20)
print("Números Informados: {}".format(numeros))
print("-=-" * 20)
print("Números Pares: {}".format(numerosPares))
print("-=-" * 20)
print("Números Impares: {}".format(numerosImpares))
print("-=-" * 20)