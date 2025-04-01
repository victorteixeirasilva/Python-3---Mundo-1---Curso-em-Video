"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

"""
nome = input("Informe seu nome completo: ")
resultado = "SILVA" in nome.upper()
print("O nome {}, tem SILVA? {}".format(nome, resultado))