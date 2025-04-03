# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente, até ter um valor correto.
from operator import truediv

sexoValido = True
while sexoValido:
    sexo = str(input("Informe o sexo (F/M): "))
    if sexo.upper() == "M":
        print("MASCULINO")
        sexoValido = False
    elif sexo.upper() == "F":
        print("FEMININO")
        sexoValido = False