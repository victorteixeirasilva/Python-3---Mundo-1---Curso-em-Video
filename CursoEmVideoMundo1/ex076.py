# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ("Produto 1", 1.2, "Produto 2", 1.3, "Produto 3", 1.5, "Produto 4", 2.4)
for c in range(0, len(produtos)-1, 2):
    print("{:<10}".format(produtos[c]), end="")
    print("."*20, end=" ")
    print("{}".format(produtos[c+1]))