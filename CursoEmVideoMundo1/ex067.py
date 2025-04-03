# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interronpido quando o número solicitado for negativo.
while True:
    print("-=-"*20)
    numero = int(input("Informe o número que seja ver a tabuada: "))
    if numero < 0:
        break
    print("-=-"*20)
    for c in range(1, 11):
        print(f"{numero} x {c} = {numero*c}")
    print("-=-"*20)

