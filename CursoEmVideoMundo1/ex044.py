"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
de pagamento.

- À vista, dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros

"""
preco = float(input("Informe o valor do produto: "))
print("1 - Para pagamento à vista, dinheiro/cheque")
print("2 - Para pagamento à vista no cartão")
print("3 - Em até 2x no cartão")
print("4 - em 3x ou mais no cartão")
opcao = int(input("Escolha a forma de pagamento: "))
if opcao == 1:
    print("O preço a ser pago é R${:.2f}".format(preco-(preco*0.1)))
elif opcao == 2:
    print("O preço a ser pago é R${:.2f}".format(preco-(preco*0.05)))
elif opcao == 3:
    print("O preço a ser pago é R${:.2f}".format(preco))
elif opcao == 4:
    print("O preço a ser pago é R${:.2f}".format(preco+(preco*0.2)))
else:
    print("Opção invalida!")
