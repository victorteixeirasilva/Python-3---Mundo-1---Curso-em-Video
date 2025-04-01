"""
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: Todos os lados iguais
- Isósceles: Dois lados iguais.
- Escaleno: Todos os lados diferentes

"""
a = int(input("Informe o comprimento da primeira reta: "))
b = int(input("Informe o comprimento da segunda reta: "))
c = int(input("Informe o comprimento da terceira reta: "))
if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    print("Pode formar um triângulo!")
    if a == b and b == c:
        print("Equilátero: Todos os lados iguais.")
    elif a == b or a == c or c == b:
        print("Isósceles: Dois lados iguais.")
    else:
        print("Escaleno: Todos os lados diferentes.")
else:
    print("Não pode formar um triângulo!")

