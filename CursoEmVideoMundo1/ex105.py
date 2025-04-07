# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
#
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
#
# Adicione também as docstrings da função.
def notas(* notas):
    quantidade_notas = 0
    maior_nota = 0
    menor_nota = 0
    média_turma = 0
    situação = ""
    for i, n in enumerate(notas):
        quantidade_notas += 1
        média_turma += n
        if n > maior_nota:
            maior_nota = n
        if menor_nota == 0 or n < menor_nota:
            menor_nota = n
    média_turma = média_turma/quantidade_notas
    if média_turma > 8:
        situação = "MUITO BOA!"
    elif média_turma >= 6:
        situação = "BOA!"
    elif média_turma < 6:
        situação = "RUIM!"
    return {
        "Quantidade de notas: ": quantidade_notas,
        "A maior nota": maior_nota,
        "A menor nota": menor_nota,
        "A média da turma": média_turma,
        "A situação da turma": situação
    }

print(notas(3, 9, 9, 9, 9, 9, 10))
