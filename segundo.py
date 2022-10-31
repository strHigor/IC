import os
import Utils.utils as utils
import camelot #pip3 install camelot-py[cv] tabula-py

if os.path.isdir('./Anexos') == True:
    arquivos_anexo = utils.listar_arquivos("./Anexos", "*.*")
    utils.excluir_arquivos(arquivos_anexo)
    os.rmdir("./Anexos")

utils.extrair_rar("Anexos.zip")