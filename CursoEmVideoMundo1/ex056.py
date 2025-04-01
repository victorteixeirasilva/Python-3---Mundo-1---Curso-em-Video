"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

-> A média de idade do grupo.
-> Qual é o nome do homem mais velho.
-> Quantas mulheres tem menos de 20 anos.

"""
nomeHMaisVelho = ""
idadeHMaisVelho = 0
mulheresMenos20 = 0
somaIdades = 0
for c in range(1, 5):
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))
    sexo = input("Informe o sexo: ")
    somaIdades += idade
    if sexo.upper().strip() == "FEMININO":
        if idade < 20:
            mulheresMenos20 += 1
    elif idadeHMaisVelho < idade:
        idadeHMaisVelho = idade
        nomeHMaisVelho = nome
print("A média da idade do grupo é {}".format(somaIdades/4))
print("O nome do homem mais velho do grupo é ({})".format(nomeHMaisVelho))
print("O grupo tem {}, mulheres com menos de 20 anos.".format(mulheresMenos20))