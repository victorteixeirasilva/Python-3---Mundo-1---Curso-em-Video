"""
Escreva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

"""

a = int(input("Informe o comprimento da primeira reta: "))
b = int(input("Informe o comprimento da segunda reta: "))
c = int(input("Informe o comprimento da terceira reta: "))
if (a + b) > c:
    if (a + c) > b:
        if (b + c) > a:
            print("Pode formar um triângulo!")
        else:
            print("Não pode formar um triângulo!")
    else:
        print("Não pode formar um triângulo!")
else:
    print("Não pode formar um triângulo!")
