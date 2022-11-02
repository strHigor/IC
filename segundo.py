import Utils.utils as utils
import os
import tabula
import csv

if os.path.isdir("./Anexos") == True:
    arquivos_anexo = utils.listar_arquivos("./Anexos", "*.*")
    utils.excluir_arquivos(arquivos_anexo)
    os.rmdir("./Anexos")

utils.extrair_rar("Anexos.zip")

arquivoPdf = "Anexos/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546.pdf"
tabula.convert_into(arquivoPdf, "Anexo_I_Original.csv", output_format="csv", pages="3-180", lattice=True)

conteudo = ""
cabecalho_parte1 = ""
cabecalho_parte2 = ""

with open("Anexo_I_Original.csv", newline="") as aquivocsv:
    anexo_Original = csv.reader(aquivocsv, delimiter=" ", quotechar="|")
    for linha in anexo_Original:
        if anexo_Original.line_num == 1:
            cabecalho_parte1 = linha[0]
            conteudo = conteudo + ", ".join(linha) + "\n"

        elif anexo_Original.line_num == 2:
            cabecalho_parte2 = linha[0]
            conteudo = conteudo + ", ".join(linha) + "\n"

        elif linha[0] != cabecalho_parte1 and linha[0] != cabecalho_parte2:
            conteudo = conteudo + " ".join(linha) + "\n"

    conteudo = conteudo.replace(",OD,", ",Seg. Odontológica,")
    conteudo = conteudo.replace(",AMB,", ",Seg. Ambulatorial,")

arquivo_csv = open("Anexo_I.csv", "w+")
arquivo_csv.write(conteudo)
arquivo_csv.close()

os.remove(os.path.join("Anexo_I_Original.csv"))