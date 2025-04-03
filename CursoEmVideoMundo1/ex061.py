# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.
termo = int(input("Informe o primeiro termo da PA: "))
razão = int(input("Informe a razão da PA: "))
print("PA: {} ".format(termo), end = " ")
contador = 1
while contador<10:
    termo = termo+razão
    print(" {} ".format(termo), end = "")
    contador += 1