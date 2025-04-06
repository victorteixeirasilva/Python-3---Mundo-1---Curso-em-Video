"""
Faça um programa que tenha uma função chamada escreva(), que recebe um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.

Ex:
escreva("Olá, Mundo!")

Saída:
~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~~
"""
def escreva(msg):
    tamanhoLinha = len(msg)*2
    print("~"*tamanhoLinha)
    print(f"{msg:^{tamanhoLinha}}")
    print("~"*tamanhoLinha)

escreva("Olá mundo!")