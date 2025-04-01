"""
Faça um programa que leia o ano qualquer e mostre se ele é bissexto.

"""
ano = int(input("Informe um ano: "))
if (ano % 4)==0:
    if(ano % 100)!=0:
            print("O ano {} é BISSEXTO!".format(ano))
    else:
        if (ano % 400) == 0:
            print("O ano {} é BISSEXTO!".format(ano))
else:
    if (ano % 400) == 0:
        print("O ano {} é BISSEXTO!".format(ano))

    print("O ano {} não é BISSEXTO!".format(ano))