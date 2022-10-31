from zipfile import ZipFile
import os
import os.path
from Utils.file_utils import FileUtils as Utils

utils = Utils("Anexos.zip")
utils.excluir_arquivos()