"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

Ex: Ana Maria de Souza
primeiro = Ana
último = Souza

"""
nome = input("Informe seu nome completo: ")
print("Primeiro = {}".format(nome.split()[0]))
print("Último = {}".format(nome.split()[len(nome.split())-1]))