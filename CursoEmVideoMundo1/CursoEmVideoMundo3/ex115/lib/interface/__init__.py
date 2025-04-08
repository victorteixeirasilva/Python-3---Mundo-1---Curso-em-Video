def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário prefiriu não digitar esse número. \033[m')
            return 0
        else:
            return n


def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    for i, item in enumerate(lista):
        print(f"{i+1} - {item}")
    print(linha())
    opc = leia_int("Sua Opção: ")
    return opc


def pessoas(lista):
    r = ""
    for i in lista:
        pessoa = f"{i}"
        pessoa = pessoa.replace(";", "."*20)
        pessoa = pessoa.replace("\n", "")
        r += f"{pessoa}\n"
    return r