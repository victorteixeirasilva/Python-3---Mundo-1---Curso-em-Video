"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:

- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sénior
- Acima: Master

"""
from datetime import date
anoNascimento = int(input("Informe o ano que o atleta nasceu: "))
anoAtual = int(date.today().year)
idade = anoAtual - anoNascimento
if idade <= 9:
    print("Mirim")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Junior")
elif idade <= 20:
    print("Sénior")
else:
    print("Master")