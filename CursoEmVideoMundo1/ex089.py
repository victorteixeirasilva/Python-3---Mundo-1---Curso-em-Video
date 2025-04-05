"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.

"""
notas = []
aluno = []
boletim = []
while True:
    aluno.append(str(input("Informe o nome do aluno: ")))
    for a in range(1, 3):
        notas.append(float(input("Informe a nota: ")))
    aluno.append(notas[:])
    notas.clear()
    boletim.append(aluno[:])
    aluno.clear()
    while True:
        r = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
        if r in "SN":
            break
    if r == "N":
        break
print("=" * 94)
print("|{:^30}|{:^30}|{:^30}|".format("ID", "Aluno", "Nota"))
print("=" * 94)
for num, alunos in enumerate(boletim):
    media = 0
    nome = ""
    for i, nota2 in enumerate(alunos):
        if i > 0:
            for nota in nota2:
                media += nota
        else:
            nome = nota2

    print("|{:^30}|{:^30}|{:^30}|".format(num, nome, (media/2)))
print("=" * 94)
ver = 0
while ver != 999:
    ver = int(input("Informe um id que você deseja ver as notas, caso queira parar digite 999: "))
    if boletim != 999:
        print(boletim[ver])