# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
tupla = ()
for c in range(1, 6):
    novaTupla = (int(input("Informe um número: ")),)
    tupla += novaTupla
print(tupla)
print()
print("O valor 9 apareceu {}x".format(tupla.count(9)))
print()
print("O valor 3 apareceu primeiro na posição {}.".format(tupla.index(3)))
print()
print("Os números pares foram: ", end="")
for c in tupla:
    if c % 2 == 0:
        print("{}".format(c), end=" ")
