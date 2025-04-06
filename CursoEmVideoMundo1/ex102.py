
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
# indique o número a calcular e o outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

# help(fatorial)
#
# fatorial(n, show=False)
# 	-> Calcula o Fatorial de um número.
# 	:param n: O número a ser calculado.
# 	:param show: (opcional) Mostra ou não a conta.
# 	:return: O valor do Fatorial de um número n.
import math


def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
	:param n: O número a ser calculado.
	:param show: (opcional) Mostra ou não a conta.
	:return: O valor do Fatorial de um número n.
    """
    resultado = 1
    for i in range(n, 0, -1):
        if show:
            print(f"{i}", end=" x " if i > 1 else " = ")
        resultado *= i
    return resultado


print(fatorial(5))
