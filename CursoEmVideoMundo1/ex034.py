"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1250,00, calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%.

"""

salario = float(input("Qual o seu salário atual: R$"))
if salario > 1250:
    print("Para o salario R${}, o aumento será de 10%, sendo assim seu salário será R${}"
          .format(salario, salario+(salario*0.1)))
else:
    print("Para o salario R${}, o aumento será de 15%, sendo assim seu salário será R${}"
          .format(salario, salario+(salario*0.15)))
