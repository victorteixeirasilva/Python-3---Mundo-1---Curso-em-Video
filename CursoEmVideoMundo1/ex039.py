"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

"""
import datetime
anoDeNascimento = int(input("Informe seu ano de nascimento: "))
anoAtual = int(datetime.date.today().year)
idade = anoAtual-anoDeNascimento
print("De acordo com seu ano de nascimento ({}), e o ano atual ({}). verificamos que você tem {}anos"
      .format(anoDeNascimento, anoAtual, idade))
if idade > 18:
    print("Já passou do tempo do alistamento. Está {} anos atrasados.".format(idade-18))
elif idade < 18:
    print("Ainda vai se alistar ao serviço militar. Deve fazer isso em {} anos.".format(18-idade))
else:
    print("É hora de se alistar!")