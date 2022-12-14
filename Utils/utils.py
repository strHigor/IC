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
    print("\nUtils - Iniciando a exclusão dos arquivos.")
    for arquivo in arquivos_anexo:
        os.remove(os.path.join(arquivo))
    
    print("Utils - Os arquivos foram excluidos com sucesso.")


def excluir_pasta_anexos(caminho, arquivo_extensao):
    if os.path.isdir(caminho) == True:
        print(f"\nUtils - Iniciando a exclusão da pasta {caminho}.")
        arquivos_anexo = listar_arquivos(caminho, arquivo_extensao)
        excluir_arquivos(arquivos_anexo)
        os.rmdir(caminho)        
        print(f"Utils - {caminho} excluido com sucesso.")
    
    else:
        print("Caminho não existente.")



def criar_rar(arquivo_rar, arquivo_anexo):
    print(f"\nUtils - Iniciando a criação do {arquivo_rar}.")
    with ZipFile(arquivo_rar, 'w') as anexo:
        if type(arquivo_anexo) == list:
            for arquivo in arquivo_anexo:
                anexo.write(arquivo)

        if type(arquivo_anexo) == str:
            anexo.write(arquivo_anexo)

    print(f"Utils - {arquivo_rar} criado com sucesso.")

def extrair_rar(arquivo_rar):
    print(f"\nUtils - Extraindo {arquivo_rar}, aguarde por favor.")
    with ZipFile(arquivo_rar, 'r') as anexo:
        anexo.extractall()

    print(f"Utils - O {arquivo_rar} foi extraido com sucesso.")