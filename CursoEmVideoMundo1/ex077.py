# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar para cada
# palavra, quais são as vogais.
palavras = ("Victor", "Lindo", "inteligente")
for c in range(0, len(palavras)):
    vogais = ""
    for count in range(0, len(palavras[c])):
        letra = str(palavras[c][count]).upper()
        if letra == "A":
            vogais += " A"
        elif letra == "E":
            vogais += " E"
        elif letra == "I":
            vogais += " I"
        elif letra == "O":
            vogais += " O"
        elif letra == "U":
            vogais += " U"
    print("{} possui as vogais {}".format(palavras[c], vogais))

