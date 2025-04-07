# Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um
# número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaint(msg):
    while True:
        valor = input(msg)
        valorInt = 0
        if valor.isnumeric():
            valorInt = int(valor)
            if valorInt.is_integer():
                return valorInt
        # else:
        #     print("ERRO: Digite um valor inteiro!")

def leiaFloat(msg):
    while True:
        valor = input(msg)
        valorFloat = float(valor)
        return valorFloat

variavel = leiaint("Informe um int: ")
print(variavel)
try:
    variavel2 = leiaFloat("Informe um float: ")
except ValueError:
    print("Erro valor Float invalido:")
    variavel2 = leiaFloat("Informe um float: ")
else:
    print(variavel2)