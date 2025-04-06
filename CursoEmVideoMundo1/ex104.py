# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante
# à função input do Python, só que fazendo validação para aceitar apenas um valor numérico.
#
# Ex: leiaint('Digite um n')
def leiaint(msg):
    while True:
        valor = input(msg)
        valorInt = 0
        if valor.isnumeric():
            valorInt = int(valor)
            if valorInt.is_integer():
                return valorInt
        else:
            print("ERRO: Digite um valor inteiro!")

variavel = leiaint("Informe um int: ")
print(variavel)