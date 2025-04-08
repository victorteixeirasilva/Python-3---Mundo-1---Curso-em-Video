# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar pessoa e listar todas as pessoas cadastradas.
from lib.interface import *
from lib.arquivo import *

arq = "curso.txt"
if arquivoExiste(arq):
    print("Arquivo encontrado com sucesso!")
else:
    print("Arquivo não encontado!")
    criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do Sistema"])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Cadastrar uma nova pessoa
        cabeçalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leia_int("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print("Saindo do Sistema... Até Logo!")
        break
    else:
        print('\n\033[31mErro: digite uma opção válida. \033[m')

