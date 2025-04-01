"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

"""
def verificar_primo(numero):
    if numero < 2:
        return False  # Números menores que 2 não são primos
    for i in range(2, int(numero ** 0.5) + 1):  # Checa divisores de 2 até a raiz quadrada do número
        if numero % i == 0:
            return False  # Se houver um divisor, não é primo
    return True  # Caso não encontre divisores, é primo

# Exemplo de uso
numero = int(input("Digite um número inteiro: "))
if verificar_primo(numero):
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")