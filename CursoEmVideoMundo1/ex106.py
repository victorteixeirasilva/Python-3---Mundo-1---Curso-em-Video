# Faça um mini-sistema que utilize o interactive Help do Python. O usuário vai digitar o
# comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa
# se encerrará.
#
# OBS: use cores.
c = (
    "\033[n",       # 0 - sem cores
    "\033[0;30;41", # 1 - vermelho
)
def ajuda(com):
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end=" ")
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)
    print(c[0], end=" ")



# Programa
comando = ""
while True:
    titulo("SISTEMA DE AJUDA PyHelp", 1)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper().strip() == "FIM":
        break
    else:
        ajuda(comando)
    titulo("ATÉ LOGO!")