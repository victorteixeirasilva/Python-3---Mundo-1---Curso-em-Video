# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
# se o usuário quer ou não continuar.
# No final, mostre:
#
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
pessoasMais18 = 0
homensCadastrados = 0
mulheresMenos20 = 0
éPraParar = False
while not éPraParar:
    sOUn = ""
    sexo = ""
    idade = int(input("Informe a idade: "))
    while sexo != "M" and sexo != "F":
        sexo = str(input("Informe o sexo [M/F]: ")).strip().upper()
    if idade >= 18:
        pessoasMais18 += 1
    if sexo == "M":
        homensCadastrados += 1
    if sexo == "F" and idade <= 20:
        mulheresMenos20 +=1
    while sOUn != "S" and sOUn != "N":
        sOUn = str(input("Deseja continuar informando pessoas [S/N]: ")).strip().upper()
    if sOUn == "N":
        break

print("-=-"*20)
print(f"Temos {pessoasMais18} pessoas com mais de 18 anos.")
print(f"{homensCadastrados} homens foram cadastrados.")
print(f"{mulheresMenos20} mulheres cadastradas tem menos de 20 anos.")
print("-=-"*20)
