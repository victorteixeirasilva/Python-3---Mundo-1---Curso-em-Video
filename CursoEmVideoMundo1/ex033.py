"""
Escreva um programa que leia três números e mostre qual é o maior e qual é o menor.

"""
n1 = int(input("Informe um número: "))
n2 = int(input("Informe um número: "))
n3 = int(input("Informe um número: "))
if n1 > n2:
    if n1 > n3:
        print("O número {} é o maior".format(n1))
    else:
        print("O número {} é o maior".format(n3))
else:
    if n2 > n3:
        print("O número {} é o maior".format(n2))
    else:
        print("O número {} é o maior".format(n3))

if n1 < n2:
    if n1 < n3:
        print("O número {} é o menor".format(n1))
    else:
        print("O número {} é o menor".format(n3))
else:
    if n2 < n3:
        print("O número {} é o menor".format(n2))
    else:
        print("O número {} é o menor".format(n3))
