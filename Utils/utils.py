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

def criar_rar(arquivo_rar, arquivos_anexo):
    with ZipFile(arquivo_rar, 'w') as anexo:
        for arquivo in arquivos_anexo:
            anexo.write(arquivo)

def extrair_rar(arquivo_rar):
    with ZipFile(arquivo_rar, 'r') as anexo:
        anexo.extractall()