"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa retornando um valor literal indicando se uma pessoa tem voto negado,
opcional ou obrigatório nas eleições.

"""
import datetime


def voto(a):
    idade = datetime.datetime.now().year - a
    if 16 <= idade < 18:
        return "Voto Opcional"
    elif idade >= 18:
        return "Voto Obrigatório"

print(voto(2003))