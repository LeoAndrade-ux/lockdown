import os

class FileManager:
    def __init__(self, destination, extensions=None):
        self.destination = destination
        self.extensions = extensions if extensions else []
        self.files = self.get_files()

    def get_files(self):
        files = []
        for root, _, filenames in os.walk(self.destination):
            for filename in filenames:
                # Si no hay extensiones especificadas, agregar todos los archivos
                if not self.extensions or any(filename.endswith(ext) for ext in self.extensions):
                    files.append(os.path.join(root, filename))  # Asegura una concatenación correcta
        return files

    def log_activity(self, action, file):
        print(f"{action}: {file}")
