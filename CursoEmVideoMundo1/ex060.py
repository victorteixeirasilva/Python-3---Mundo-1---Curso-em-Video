# Faça um programa que leia um número qualquer e mostre o seu fatorial
#
# Ex:
# 5! = 5x4x3x2x1 = 120
numero = int(input("Informe um número: "))
resultado = ""
resultado += str(numero)
resultado += "!"
resultado += " = "
resultado += str(numero)
contador = numero
resultadoMultiplicação = numero
while contador>1:
    resultadoMultiplicação *= contador-1
    resultado += "x"
    resultado += str(contador-1)
    contador = contador - 1
resultado += " = "
resultado += str(resultadoMultiplicação)
print(resultado)

