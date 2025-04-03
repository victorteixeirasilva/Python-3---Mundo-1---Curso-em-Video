# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
# Sequência de Fibonacci.
#
# Ex:
# 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
elementos = int(input("Informe quantos elementos quer ver da sequencia Fibonacci: "))
elementoAnterior = 1
elementoAtual = 2
contadorDeElementos = 4
print("0 -> 1 -> 1 -> 2", end=" ")
while contadorDeElementos < elementos:
    temp = elementoAtual + elementoAnterior
    print("-> {}".format(temp), end = " ")
    elementoAnterior = elementoAtual
    elementoAtual = temp
    contadorDeElementos += 1