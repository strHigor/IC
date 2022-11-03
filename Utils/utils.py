import os
import os.path
from pathlib import Path
from zipfile import ZipFile


def listar_arquivos(caminho, extensao):
    arquivos = []
    for arquivo in Path(caminho).glob(extensao):
        arquivos.append(arquivo)
    return arquivos


def excluir_arquivos(arquivos_anexo):
    for arquivo in arquivos_anexo:
        os.remove(os.path.join(arquivo))


def excluir_pasta_anexos(caminho, arquivo_extensao):
    if os.path.isdir(caminho) == True:
        arquivos_anexo = listar_arquivos(caminho, arquivo_extensao)
        excluir_arquivos(arquivos_anexo)
        os.rmdir(caminho)


def criar_rar(arquivo_rar, arquivo_anexo):
    with ZipFile(arquivo_rar, 'w') as anexo:
        if type(arquivo_anexo) == list:
            for arquivo in arquivo_anexo:
                anexo.write(arquivo)

        if type(arquivo_anexo) == str:
            anexo.write(arquivo_anexo)


def extrair_rar(arquivo_rar):
    with ZipFile(arquivo_rar, 'r') as anexo:
        anexo.extractall()
