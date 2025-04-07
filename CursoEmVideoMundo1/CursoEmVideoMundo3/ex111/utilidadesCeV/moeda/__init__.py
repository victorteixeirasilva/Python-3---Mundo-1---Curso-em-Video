def aumentar(n, p, formatar=True):
    if formatar:
        return moeda(n+(n * (p/100)))
    else:
        return n+(n * (p/100))

def diminuir(n, p, formatar=True):
    if formatar:
        return moeda(n - (n * (p / 100)))
    else:
        return n - (n * (p / 100))


def dobro(n, formatar=True):
    if formatar:
        return moeda(n*2)
    else:
        return n*2


def metade(n, formatar=True):
    if formatar:
        return moeda(n/2)
    else:
        return n/2


def moeda(n):
    return f"R${n:.2f}"


def resumo(n, a=50, d=50):
    print("~" * 16)
    print(f"{"RESUMO":^16}")
    print("~" * 16)
    print("{:^16}".format(dobro(n)))
    print("{:^16}".format(metade(n)))
    print("{:^16}".format(aumentar(n, a)))
    print("{:^16}".format(diminuir(n, d)))
    print("~" * 16)
