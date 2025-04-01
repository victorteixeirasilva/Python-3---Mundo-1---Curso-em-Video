"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

"""
cidade = input("Informe um nome de uma cidade: ")
print("A cidade começa com 'Santo' : {}".format(cidade.upper().startswith("SANTO")))