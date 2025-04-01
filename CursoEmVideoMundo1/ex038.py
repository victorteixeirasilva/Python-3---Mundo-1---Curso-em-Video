"""
Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:

- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.

"""
numeroUm = int(input("Informe um número: "))
numeroDois = int(input("Informe outro número: "))
if numeroUm > numeroDois:
    print("O primeiro valor é maior.")
elif numeroDois > numeroUm:
    print("O segundo valor é maior,")
else:
    print("Não existe valor maior, os dois são iguais.")