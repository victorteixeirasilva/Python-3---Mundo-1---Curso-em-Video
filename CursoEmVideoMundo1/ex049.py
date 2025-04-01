"""
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

"""
number = int(input("Informe um número: "))
print("*** TABUADA ***")
for tabuada in range(1, 11):
    print("{} X {} = {}".format(number, tabuada, number*tabuada))

