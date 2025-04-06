"""
Faça um programa que tenha uma função chamada maior(), que recebe vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

"""
def maior(* num):
    tamanho = len(num)*2
    print("-=-"*tamanho)
    print(num)
    lista = sorted(num).copy()
    print(f"O maior número informado é {lista[len(lista)-1]}")
    print("-=-"*tamanho)


maior(5, 10, 4, 12, 23)