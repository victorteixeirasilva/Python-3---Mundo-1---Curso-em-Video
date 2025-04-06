"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
(com idade em) um dicionário se por acaso a CTPS for diferente de Zero, o dicionário
também recebera o ano de contratação e o salário. Calcule e acrescente, além da idade
com quantos anos a pessoa vai se aposentar.

"""
import datetime
funcionario = dict()
funcionario["nome"] = input("Informe o nome do funcionário: ")
anoDeNascimento = int(input("Informe o ano de nascimento: "))
anoAtual = datetime.date.today().year
idade = anoAtual - anoDeNascimento
funcionario["idade"] = idade
funcionario["CTPS"] = int(input("Informe a carteira de tabalho: "))
if funcionario["CTPS"] != 0:
    funcionario["Ano De Contratação"] = int(input("Ano de contratação: "))
    anosTrabalhados = anoAtual - funcionario["Ano De Contratação"]
    funcionario["Idade Para se Aposentar"] = (55-anosTrabalhados)+funcionario["idade"]
print(funcionario)