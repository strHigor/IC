import os
import os.path
from pathlib import Path
from zipfile import ZipFile


class FileUtils:
    def __init__(self, arquivo_rar):
        self.arquivo_rar = arquivo_rar
        self.arquivos_anexo = []

    def listar_arquivos(self, caminho, extensao):
        arquivos = []
        for arquivo in Path(caminho).glob(extensao):
            arquivos.append(arquivo)
        return arquivos

    def excluir_arquivos(self):
        for arquivo in self.arquivos_anexo:
            os.remove(os.path.join(arquivo))

    def criar_rar(self):
        with ZipFile(self.arquivo_rar, 'w') as anexo:
            for arquivo in self.arquivos_anexo:
                anexo.write(arquivo)