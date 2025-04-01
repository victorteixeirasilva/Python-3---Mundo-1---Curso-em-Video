"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão.

"""
def mostrar_progressao(primeiro_termo, razao):
    termos = []
    for i in range(10):  # Calcula os 10 primeiros termos
        termo = primeiro_termo + i * razao
        termos.append(termo)
    return termos

# Exemplo de uso
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

progressao = mostrar_progressao(primeiro_termo, razao)
print("Os 10 primeiros termos da PA são:")
print(progressao)
