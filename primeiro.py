import wget
import os
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import Utils.utils as utils

arquivos = []

def requisicao():
    try:
        if os.path.isdir("./Anexos") == False:
            os.mkdir("./Anexos")

        conteudo = requests.get("https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude")
        if conteudo.status_code != 200:
            return

        site = BeautifulSoup(conteudo.text, "html5lib")

        for x in range(14, 19):
            link = site.select(f"#parent-fieldname-text > p:nth-child({str(x)}) > a")[0].attrs["href"]
            wget.download(link, "./Anexos")

        for arquivo in Path("./Anexos").glob("*.*"):
            arquivos.append(arquivo)

        arquivos_anexo = utils.listar_arquivos("./Anexos", "*.*")
        utils.criar_rar("Anexos.zip", arquivos_anexo)
        utils.excluir_arquivos(arquivos_anexo)
        os.rmdir("./Anexos")

        return
    except Exception as erro:
        print(str(erro))

requisicao()