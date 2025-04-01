"""
Escreva um programa que leia a velocidade de um carro.

Se ela ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$ 7,00 por cada Km acima do limite.

"""

velocidade = int(input("Informe a velocidade do carro: "))
if velocidade > 80:
    print("Você foi multado! pois está acima do limite de velocidade")
    print("O valor da multa é de R${:.2f}".format(7*(velocidade-80)))
else:
    print("Você estava dentro do limite!")
