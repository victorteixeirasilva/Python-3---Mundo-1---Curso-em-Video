"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

"""
frase = input("Digite uma frase: ")
fraseSemEspacos = frase.upper().replace(" ", "").strip()
fraseInvertida = ""
palindromo = True
for c in range(len(fraseSemEspacos)-1, -1, -1):
    fraseInvertida += fraseSemEspacos[c]
for c in range(0, len(fraseSemEspacos)):
    if fraseSemEspacos[c] != fraseInvertida[c]:
        palindromo = False
if palindromo:
    print("A frase ({}), é um palíndromo!".format(frase))
else:
    print("A frase ({}), não é um palíndromo!".format(frase))
print(fraseSemEspacos)
print(fraseInvertida)
