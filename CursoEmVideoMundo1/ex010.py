# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

# Considere US$ 1.00 = R$ 3.27

balance = float(input("Informe o valor que tem na sua carteira: "))
print("Com esse valor na carteira ({}), e levando em consideração o dolar á (US$ 1.0), podemos comprar {} dolares"
      .format(balance, balance/3.27))