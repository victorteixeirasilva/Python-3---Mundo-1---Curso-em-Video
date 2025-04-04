# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso mostre:
#
# A) Quantos números foram digitados.
# B) A lista de valores ordenada em ordem decrescente.
# C) Se o valor 5 foi digitado e se está ou não na lista.
numeros = []
count = 0
resposta5 = "não foi"
while True:
    numero = int(input("Informe um número: "))
    if numero == 5:
        resposta5 = "foi"
    numeros.append(numero)
    while True:
        r = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
        if r in "SN":
            break
    if r in "Nn":
        break
print("-=-" * 10)
print(f"Foram digitados {len(numeros)} números.")
print("-=-" * 10)
numeros.sort(reverse=True)
print(numeros)
print("-=-" * 10)
print(f"O valor 5 {resposta5} digitado.")
print("-=-" * 10)
