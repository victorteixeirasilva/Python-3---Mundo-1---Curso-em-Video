from ..interface import cabeçalho
from ..interface import pessoas

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\n\033[31mHouve um ERRO na criação do arquivo! \033[m')
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print('\n\033[31mHouve um ERRO ao ler o arquivo! \033[m')
    else:
        cabeçalho("PESSOAS CADASTRADAS")
        print(pessoas(a.readlines()))
    finally:
        a.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('\n\033[31mHouve um ERRO ao ler o arquivo! \033[m')
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print('\n\033[31mHouve um ERRO ao cadastrar pessoa no arquivo! \033[m')
        else:
            print(f"Novo registro de {nome} adicionado.")
    finally:
        a.close()
