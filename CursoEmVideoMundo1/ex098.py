"""
Faça um programa que tenha uma função chamada contador(), que recebe três parâmetros: início, fim e passo e realize a
contagem.

Seu programa tem que realizar três contagens através da função criada:

A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada
"""
import time
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio > fim and passo > 0:
        passo = passo - (passo * 2)
    print("-=-"*20)
    if passo > 0:
        fim += 1
    else:
        fim -= 1
    print(f"Contagem -> Inicio: {inicio}, Fim: {fim}, Passo: {passo}")
    print("Contando...")
    time.sleep(1)
    for i in range(inicio, fim, passo):
        print(f"{i} ", end="")
        time.sleep(0.5)
    print()
    print("-=-"*20)


contador(1, 10, 1)
contador(10, 0, 2)
while True:
    inicio = int(input("Informe o início da sua contagem: "))
    fim = int(input("Informe o fim da sua contagem: "))
    if inicio != fim:
        break
passo = int(input("Informe o passo da sua contagem: "))
contador(inicio, fim, passo)
