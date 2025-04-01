"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal

"""
numero = int(input("Informe um inteiro: "))
print("O número informado foi ({}).".format(numero))
print("1 - para ver fazer a conversão para binário")
print("2 - para ver fazer a conversão para octal")
print("3 - para ver fazer a conversão para hexadecimal")
opcao = int(input("Escolha uma das 3 opções: "))
if opcao==1:
    print(bin(numero))
elif opcao==2:
    print(oct(numero))
elif opcao==3:
    print(hex(numero))
else:
    print("Opção inválida!")
