"""
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

"""
valorDaCasa = float(input("Informe o valor da casa que deseja comprar: "))
salario = float(input("Informe o valor do salário do comprador: "))
anos = int(input("Informe a quantidade de anos que deseja pagar a casa: "))
trintaPorcentoDoSalario = salario*0.3
parcelas = valorDaCasa/(anos*12)
if parcelas < trintaPorcentoDoSalario:
    print("Empréstimo aprovado!")
    print("O valor da prestação mensal é R${:.2f}".format(parcelas))
else:
    print("Empréstimo negado!")
