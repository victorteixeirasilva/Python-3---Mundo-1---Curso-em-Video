"""
Crie um programa que leia o nome completo de uma pessoa e mostre

-> O nome com todas as letras maiúsculas.

-> O nome com todas as letras minúsculas.

-> Quantas letras ao todo.

-> Quantas letras tem o primeiro nome.

"""

nomeCompleto = input("Digite seu nome completo: ")
print("Nome com todas as letras maiúsculas {}".format(nomeCompleto.upper()))
print("Nome com todas as letras minúsculas {}".format(nomeCompleto.lower()))
print("Quantidade de letras presentes no nome, sem considerar os espaços é {}"
      .format(len(nomeCompleto.replace(" ", ""))))
print("Quantidade de Letras presentes no primeiro nome é {}"
      .format(len(nomeCompleto.split()[0])))
