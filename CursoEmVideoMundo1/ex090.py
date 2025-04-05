"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final mostre
o conteúdo da estrutura na tela.

"""
nome = input("Informe o nome do aluno: ")
média = float(input("Informe a média desse aluno: "))
aluno = {"nome":nome, "média":média, "estado":""}
estado = ""
if média >= 6:
    estado = "APROVADO"
else:
    estado = "REPROVADO"
aluno["estado"] = estado
print(aluno)