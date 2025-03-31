# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a qunatidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma
# área de 2,m^2.

largura = float(input("Informe a largura da parede: "))
altura = float(input("Informe a altura da parede: "))
print("A parede tem {} metros quadrados, são necessário {} litros de tinta para pintala."
      .format(largura*altura, (largura*altura)/2))