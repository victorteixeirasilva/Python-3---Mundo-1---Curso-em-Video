"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final mostre:

A) Quantas pessoas foram cadastradas.

B) A média de idade do grupo.

C) Uma lista com todas as mulheres.

D) Uma lista com todas as pessoas com idade acima da média.

"""
pessoa = dict()
grupo = list()
somaIdades = 0
grupoF = list()
while True:
    pessoa["nome"] = input("Informe o nome da pessoa: ")
    while True:
        sx = input("Informe o sexo [M/F]: ").strip().upper()[0]
        if sx in "MF":
            break
    pessoa["sexo"] = sx
    pessoa["idade"] = int(input("Informe a idade: "))
    somaIdades += pessoa["idade"]
    print(f"Os dados informado foram nome={pessoa["nome"]}, sexo={pessoa["sexo"]}, idade={pessoa["idade"]}")
    grupo.append(pessoa.copy())
    if sx == "F":
        grupoF.append(pessoa.copy())
    pessoa.clear()
    while True:
        r = input("Desseja adicionar outra pessoa [S/N]: ").strip().upper()[0]
        if r in "SN":
            break
    if r == "N":
        break
print(f"O total de pessoas cadastradas foi {len(grupo)}")
media = somaIdades/len(grupo)
print(f"A media da idade das pessoas é {media}")
print("-"*60)
print("As Mulheres adicionadas foram: ")
for m in grupoF:
    print(m)
print("-"*60)
print("As pessoas com idade acima da média são: ")
for p in grupo:
    if p["idade"] >= media:
        print(p)
print("-"*60)
