# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
#
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais Barato.

finalizar = False
totalGasto = 0
qtd1000 = 0
produtoMaisBaratoNome = ""
produtoMaisBaratoPreço = 0
while not finalizar:
    simOuNão = ""
    preço = -2
    produto = str(input("Informe o nome do produto: "))
    while preço < 0:
        preço = float(input("Informe o preço do produto: "))
    totalGasto += preço
    if preço >= 1000:
        qtd1000 += 1
    if produtoMaisBaratoNome == "":
        produtoMaisBaratoNome = produto
        produtoMaisBaratoPreço = preço
    elif preço < produtoMaisBaratoPreço:
        produtoMaisBaratoNome = produto
        produtoMaisBaratoPreço = preço
    while simOuNão != "S" and simOuNão != "N":
        simOuNão = str(input("Deseja continuar [S/N]: ")).strip().upper()
    if simOuNão == "N":
        break
print("-=-"*20)
print("O total gasto na compra foi R${:.2f}".format(totalGasto))
print(f"{qtd1000} produtos custam mais que R$1.000,00")
print(f"O produto mais barato comprado foi {produtoMaisBaratoNome}.")
print("-=-"*20)