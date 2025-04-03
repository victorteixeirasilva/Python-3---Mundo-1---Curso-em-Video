# Melhore o DESAFIO 061, pergunte para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.
desejaContinuar = True
numeroDeTermos = 10
termo = int(input("Informe o primeiro termo da PA: "))
razão = int(input("Informe a razão da PA: "))
while desejaContinuar:
    print("PA: {} ".format(termo), end = " ")
    contador = 1
    while contador < numeroDeTermos:
        termo = termo+razão
        print(" {} ".format(termo), end = "")
        contador += 1
    desejaVerMaisTermos = str(input("[S/N]: "))
    if desejaVerMaisTermos.upper() == "S":
        numeroDeTermos = int(input("Informe mais quantos termos deseja ver: "))
    elif desejaVerMaisTermos.upper() == "N":
        desejaContinuar = False
    else:
        print("Opção inválida!")