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