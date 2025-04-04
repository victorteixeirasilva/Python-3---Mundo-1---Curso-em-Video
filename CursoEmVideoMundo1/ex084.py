"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.

B) Uma listagem com as pessoas mais pesadas.

C) Uma listagem com as pessoas mais leves.

Retorno:
Ao todo, você cadastrou 6 pessoas.
O maior peso foi de 100.0Kg. Peso de [ex:João] [ex:Hélio]
O menor peso foi de 70.0Kg. Peso de [ex:Maria] [ex:Ana]

"""
pessoa = []
pessoas = []
while True:
    pessoa.append(str(input("Informe o nome da pessoa: ")))
    pessoa.append(float(input("Informe o peso da pessoa em Kg: ")))
    pessoas.append(pessoa[:])
    pessoa.clear()
    while True:
        r = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
        if r in "SN":
            break
    if r == "N":
        break
maiorPeso = 0
menorPeso = 0
for pes in pessoas:
    if maiorPeso < pes[1]:
        maiorPeso = pes[1]
    if menorPeso == 0 or menorPeso > pes[1]:
        menorPeso = pes[1]
pessoasMenorPeso = []
pessoasMaiorPeso = []
for pes in pessoas:
    if pes[1] == maiorPeso:
        pessoasMaiorPeso.append(pes[0])
    elif pes[1] == menorPeso:
        pessoasMenorPeso.append(pes[0])
print("-=-" * 10)
print(f"Você cadastrou {len(pessoas)} pessoas.")
print("-=-" * 10)
print(f"O maior peso foi de {maiorPeso}Kg. Peso de {pessoasMaiorPeso}")
print("-=-" * 10)
print(f"O menor peso foi de {menorPeso}Kg. Peso de {pessoasMenorPeso}")