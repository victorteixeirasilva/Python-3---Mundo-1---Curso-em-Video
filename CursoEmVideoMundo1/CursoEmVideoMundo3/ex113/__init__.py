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
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print("Erro valor Float invalido:")
            continue


variavel = leiaint("Informe um int: ")
print(variavel)
variavel2 = leiaFloat("Informe um float: ")
print(variavel2)