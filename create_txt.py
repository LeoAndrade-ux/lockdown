import os
username = os.getlogin()
destination = r'/home/cybersleuth/ransomware_dir'

nombre = "ransonware.txt"
ruta_completa = os.path.join(destination,nombre)

with open(ruta_completa, 'w+') as archivo:
    archivo.write("Test")