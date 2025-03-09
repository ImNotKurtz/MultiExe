import os
import subprocess
import sys
import shutil
import tempfile

# Pasta temporária onde os arquivos .exe serão extraídos
temp_path = tempfile.mkdtemp()

# Obtém dinamicamente todos os arquivos .exe dentro do sys._MEIPASS
files = [f for f in os.listdir(sys._MEIPASS) if f.endswith(".exe")]

# Extrai os arquivos para a pasta temporária
for file in files:
    with open(os.path.join(temp_path, file), "wb") as out:
        out.write(open(os.path.join(sys._MEIPASS, file), "rb").read())

# Executa os arquivos extraídos
for file in files:
    subprocess.Popen(os.path.join(temp_path, file), shell=True)
