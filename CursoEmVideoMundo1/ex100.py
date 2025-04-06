"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocálos dentro da lista e a segunda função vai mostrar a soma entre todos os valores
pares sorteados pela função anterior.

"""
import random
import time

def sortear():
    lista = list()
    print("-=-"*30)
    print("Sorteando...")
    time.sleep(1)
    for i in range(1, 6):
        lista.append(int(random.randrange(1, 50)))
    print("Os números sorteados foram: ", end="")
    for n in lista:
        print(f"{n} ", end="")
    print()
    print("-=-"*30)
    return lista.copy()


def somaPar(numeros):
    somaP = 0
    for n in numeros:
        if n % 2 == 0:
            somaP += n
    print(f"A soma dos valores pares é {somaP}")

numeros = sortear()
somaPar(numeros)