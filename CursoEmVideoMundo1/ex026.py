"""
Faça um programa que leia uma frase pelo teclado e mostre:

-> Quantas vezes aparece a letra "A".

-> Em qual posição ela aparece a primeira vez.

-> Em que posição ela aparece a última vez.

"""

frase = input("Digite algo: ")
print("A letra (A) aparece ({}x)".format(frase.upper().count("A")))
print("A letra (A) aparece primeiro na posição ({})".format(frase.upper().find("A")))
print("A letra (A) aparece por último na posição ({})".format(frase.upper().rfind("A")))